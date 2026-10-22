# """Demo for Extension 3: CousinLift (a free ride that does not inherit Transport).
# demo_mukisa_b306672.py
# """
# from story import CousinLift, Transport, Journey, compare


# def show(label, expected, actual):
#     status = "PASS" if expected == actual else "FAIL"
#     print(f"  {label}")
#     print(f"    expected: {expected}")
#     print(f"    actual:   {actual}")
#     print(f"    {status}")


# # Each check uses its own objects so one check cannot affect another.

# print("CHECK 1: CousinLift works inside compare() (duck typing)")
# lift = CousinLift("Moris")
# compare([lift], 5)  # Prints describe() and the quote.
# show("is it a Transport subclass?", False, isinstance(lift, Transport))

# print("\nCHECK 2 (normal case): Amina takes the lift with money in her purse")
# amina = Journey("Amina", 5000)
# result = amina.travel(CousinLift("Moris"), 5)
# show("message", "Amina travels by Moris: UGX 0.", result)
# show("money left", 5000, amina.purse.balance)  # Free means nothing is spent.
# show("completed legs", 1, amina.completed_legs)

# print("\nCHECK 3 (boundary case): Peter has UGX 0 and can still take the lift")
# peter = Journey("Peter", 0)
# result = peter.travel(CousinLift("Moris"), 3)
# show("message", "Peter travels by Moris: UGX 0.", result)
# show("money left", 0, peter.purse.balance)
# show("completed legs", 1, peter.completed_legs)

# print("\nCHECK 4 (refused case): distance 0 is not a valid trip")
# malish = Journey("Malish", 3000)
# result = malish.travel(CousinLift("Moris"), 0)
# show("message", "Distance must be positive. No trip started.", result)
# show("money left", 3000, malish.purse.balance)  # Nothing changed.
# show("completed legs", 0, malish.completed_legs)  # Refused trip not counted.


"""StrictJourney only adds a *checked* entry point (safe_travel). The original
Journey.travel keeps its friendly-message behaviour for the baseline story.
"""
from story import Journey


class JourneyChoiceError(Exception):
    "No usable choice object was supplied (for example None)."




class JourneyRequestError(Exception):
    "The request itself is invalid: bad distance or a negative requirement."


class JourneyResourceError(Exception):
    "The request is valid, but more UGX is needed than remain."


def _is_whole_number(value):
    return isinstance(value, int) and not isinstance(value, bool)


class StrictJourney(Journey):
    def safe_travel(self, choice, distance):
        """Validate everything first; only then delegate to travel().

        Every check happens before any money moves or history changes, so a
        raised exception always means nothing was spent or recorded.
        """
        # `is None`, not `if not choice`: a zero-cost choice is still a choice.
        if choice is None:
            raise JourneyChoiceError("No transport choice was supplied.")
        if not (hasattr(choice, "quote_fare") and hasattr(choice, "name")):
            raise JourneyChoiceError(
                "That object cannot quote a fare, so it is not a transport choice.")

        if not _is_whole_number(distance) or distance <= 0:
            raise JourneyRequestError(
                f"Distance must be a positive whole number, got {distance!r}.")

        fare = choice.quote_fare(distance)  # Asking costs nothing.
        if not _is_whole_number(fare):
            raise JourneyRequestError(
                f"{choice.name} quoted {fare!r}, which is not a whole number of UGX.")
        if fare < 0:
            raise JourneyRequestError(
                f"{choice.name} quoted a negative requirement (UGX {fare:,}).")

        if fare > self.purse.balance:
            raise JourneyResourceError(
                f"{choice.name} needs UGX {fare:,} but only "
                f"UGX {self.purse.balance:,} remain.")

        return self.travel(choice, distance)  # Existing behaviour does the work.