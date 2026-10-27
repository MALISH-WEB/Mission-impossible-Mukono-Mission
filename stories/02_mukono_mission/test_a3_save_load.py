"""Automated checks for A3: save a Journey to JSON and load it again.

Run from the main repository folder:
  py -3 -m unittest discover -s stories/02_mukono_mission -p "test_*.py"
"""
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from story import (Boda, CheerfulStudentBoda, CousinLift, Journey, Shuttle,
                   StudentBoda, Taxi, Transport, WalkWithFriend)


class SaveLoadChecks(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.folder = Path(folder.name)

    def write(self, name, data):
        path = self.folder / name
        path.write_text(data if isinstance(data, str) else json.dumps(data),
                        encoding="utf-8")
        return path

    # Normal cases
    def test_round_trip_keeps_money_count_and_labels(self):
        amina = Journey("Amina", 9000)
        amina.travel(StudentBoda("Nambi"), 3)
        amina.travel(Taxi("Mukono taxi"), 3)
        path = self.folder / "amina.json"
        amina.save(path)
        loaded = Journey.load(path)
        self.assertEqual(loaded.student, "Amina")
        self.assertEqual(loaded.purse.balance, amina.purse.balance)
        self.assertEqual(loaded.completed_legs, 2)
        self.assertEqual([l.name for l in loaded._legs],
                         [l.name for l in amina._legs])

    def test_loaded_journey_is_new_with_fresh_objects(self):
        amina = Journey("Amina", 5000)
        amina.travel(Boda("Kato"), 2)
        path = self.folder / "a.json"
        amina.save(path)
        loaded = Journey.load(path)
        self.assertIsNot(loaded, amina)
        self.assertIsNot(loaded.purse, amina.purse)
        self.assertIsNot(loaded._legs[0], amina._legs[0])
        loaded.travel(Taxi("T"), 3)
        self.assertEqual(amina.completed_legs, 1)  # Original untouched.

    def test_loaded_journey_can_continue(self):
        amina = Journey("Amina", 5000)
        amina.travel(StudentBoda("Nambi"), 3)  # 2500 spent
        path = self.folder / "a.json"
        amina.save(path)
        loaded = Journey.load(path)
        loaded.travel(Taxi("Mukono taxi"), 3)
        self.assertEqual(loaded.purse.balance, 500)
        self.assertEqual(loaded.completed_legs, 2)

    def test_every_supported_choice_round_trips(self):
        choices = [Boda("A"), StudentBoda("B"), CheerfulStudentBoda("C"),
                   Taxi("D"), Shuttle("E"), CousinLift("F"), WalkWithFriend()]
        j = Journey("Peter", 100000)
        for choice in choices:
            j.travel(choice, 2)
        path = self.folder / "all.json"
        j.save(path)
        loaded = Journey.load(path)
        self.assertEqual([type(l) for l in loaded._legs], [type(c) for c in choices])
        self.assertEqual([l.name for l in loaded._legs], [c.name for c in choices])
        self.assertEqual(loaded.purse.balance, j.purse.balance)
        self.assertEqual(loaded.diary(), j.diary())

    # Boundary cases
    def test_empty_history_and_zero_balance_round_trip(self):
        j = Journey("Brian", 0)
        path = self.folder / "b.json"
        j.save(path)
        loaded = Journey.load(path)
        self.assertEqual((loaded.purse.balance, loaded.completed_legs), (0, 0))

    def test_saved_file_is_plain_data(self):
        j = Journey("Amina", 5000)
        j.travel(Boda("Kato"), 1)
        path = self.folder / "plain.json"
        j.save(path)
        self.assertEqual(json.loads(path.read_text(encoding="utf-8")),
                         {"version": 1, "student": "Amina", "remaining_ugx": 4000,
                          "history": [{"type": "boda", "rider": "Kato"}]})

    # Refused cases
    def assert_load_refused(self, path, error=ValueError):
        with self.assertRaises(error):
            Journey.load(path)

    def test_missing_file(self):
        self.assert_load_refused(self.folder / "nope.json", FileNotFoundError)

    def test_malformed_json(self):
        self.assert_load_refused(self.write("bad.json", '{"student": '))

    def test_not_a_record(self):
        self.assert_load_refused(self.write("list.json", "[1, 2]"))

    def test_negative_balance(self):
        self.assert_load_refused(self.write(
            "n.json", {"version": 1, "student": "A", "remaining_ugx": -1, "history": []}))

    def test_bad_balance_types(self):
        for i, bad in enumerate([2.5, "100", True, None]):
            with self.subTest(bad=bad):
                self.assert_load_refused(self.write(
                    f"b{i}.json", {"version": 1, "student": "A", "remaining_ugx": bad, "history": []}))

    def test_missing_or_bad_student_and_legs(self):
        cases = [{"remaining_ugx": 1, "history": []},
                 {"student": "", "remaining_ugx": 1, "history": []},
                 {"version": 1, "student": "A", "remaining_ugx": 1},
                 {"version": 1, "student": "A", "remaining_ugx": 1, "history": "none"}]
        for i, data in enumerate(cases):
            with self.subTest(data=data):
                self.assert_load_refused(self.write(f"c{i}.json", data))

    def test_unknown_type_label(self):
        self.assert_load_refused(self.write(
            "u.json", {"version": 1, "student": "A", "remaining_ugx": 1,
                       "history": [{"type": "UnknownRide"}]}))

    def test_labels_are_never_executed(self):
        for i, label in enumerate(["__import__('os').system('echo hi')",
                                   "Transport", "Journey", "CousinLift.__init__"]):
            with self.subTest(label=label):
                self.assert_load_refused(self.write(
                    f"e{i}.json", {"version": 1, "student": "A", "remaining_ugx": 1,
                                   "history": [{"type": label, "name": "x"}]}))

    def test_leg_missing_or_bad_field(self):
        for i, leg in enumerate([{"type": "boda"}, {"type": "taxi", "name": 5},
                                 {"type": "taxi", "name": ""}, "boda"]):
            with self.subTest(leg=leg):
                self.assert_load_refused(self.write(
                    f"f{i}.json", {"version": 1, "student": "A", "remaining_ugx": 1, "history": [leg]}))

    def test_one_bad_leg_rejects_whole_file(self):
        self.assert_load_refused(self.write(
            "m.json", {"version": 1, "student": "A", "remaining_ugx": 1,
                       "history": [{"type": "walk_with_friend"}, {"type": "Nope"}]}))

    def test_failed_load_leaves_running_session_unchanged(self):
        running = Journey("Amina", 5000)
        running.travel(Boda("Kato"), 2)
        before = (running.student, running.purse.balance, list(running._legs))
        for path in [self.folder / "missing.json",
                     self.write("x.json", "{oops"),
                     self.write("y.json", {"version": 1, "student": "A", "remaining_ugx": -5, "history": []})]:
            with self.assertRaises((FileNotFoundError, ValueError)):
                Journey.load(path)
        self.assertEqual((running.student, running.purse.balance, running._legs),
                         before)

    def test_extra_key_and_bad_version_refused(self):
        base = {"version": 1, "student": "A", "remaining_ugx": 1, "history": []}
        self.assert_load_refused(self.write("k.json", dict(base, extra=1)))
        self.assert_load_refused(self.write("v.json", dict(base, version=2)))
        self.assert_load_refused(self.write(
            "x.json", dict(base, history=[{"type": "boda", "rider": "K", "x": 1}])))

    def test_unsupported_choice_is_not_saved_and_writes_nothing(self):
        class Rocket(Transport):
            def quote_fare(self, distance):
                return 10
        j = Journey("A", 1000)
        j.travel(Rocket("Rocket"), 1)
        path = self.folder / "r.json"
        with self.assertRaises(ValueError):
            j.save(path)
        self.assertFalse(path.exists())


if __name__ == "__main__":
    unittest.main()
