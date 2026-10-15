"""Demo for Extension 5: Trip diary (Journey.diary).
Malish Emmanuel Abui, access number B33239.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from story import (Boda, CheerfulStudentBoda, Journey, Taxi,  # noqa: E402
                   WalkWithFriend, compare)


def check(label, expected, actual):
    status = "PASS" if expected == actual else "FAIL"
    print(f"[{status}] {label}")
    print(f"   expected: {expected}")
    print(f"   actual:   {actual}")


def main():
    # The existing options list and compare() are reused, not changed.
    options = [Boda("Kato"), Taxi("Mukono taxi"),
               CheerfulStudentBoda("Nambi"), WalkWithFriend()]
    print("--- Options from the original story ---")
    compare(options, 3)

    print("\n=== NORMAL CASE: two completed legs ===")
    amina = Journey("Amina", 5000)
    print(amina.travel(options[2], 3))  # Student boda: UGX 2,500.
    print(amina.travel(options[1], 3))  # Taxi: UGX 2,000.
    check("diary lists both legs, count 2, UGX 500 left",
          "Amina's diary: Nambi's boda, Mukono taxi. "
          "Completed legs: 2. Money left: UGX 500.",
          amina.diary())

    print("\n=== REFUSED CASE: a refused trip is not counted ===")
    print(amina.travel(options[0], 3))  # Boda costs 3,000; only 500 left.
    check("diary is unchanged after the refused attempt",
          "Amina's diary: Nambi's boda, Mukono taxi. "
          "Completed legs: 2. Money left: UGX 500.",
          amina.diary())

    print("\n=== BOUNDARY CASE: empty journey ===")
    kato = Journey("Kato", 3000)
    check("diary with no legs shows full money",
          "Kato's diary: no completed legs. Money left: UGX 3,000.",
          kato.diary())

    print("\n=== READ-ONLY CHECK: diary() changes nothing ===")
    peter = Journey("Peter", 2000)
    peter.travel(options[3], 3)  # Free walk: completed leg, no money spent.
    legs_before = peter.completed_legs
    money_before = peter.purse.balance
    peter.diary()
    peter.diary()  # Calling it twice must not change anything either.
    check("completed legs unchanged", legs_before, peter.completed_legs)
    check("money unchanged", money_before, peter.purse.balance)
    check("free walk counted as one leg",
          "Peter's diary: Walk with a friend. "
          "Completed legs: 1. Money left: UGX 2,000.",
          peter.diary())

    print("\n=== INVALID DISTANCE: no trip, so nothing in the diary ===")
    zed = Journey("Zed", 1000)
    print(zed.travel(options[3], 0))
    check("diary still empty",
          "Zed's diary: no completed legs. Money left: UGX 1,000.",
          zed.diary())


if __name__ == "__main__":
    main()