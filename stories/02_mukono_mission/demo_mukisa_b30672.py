"""Demo for Extension 3: CousinLift (a free ride that does not inherit Transport).
demo_mukisa_b306672.py
"""
from story import CousinLift, Transport, Journey, compare


def show(label, expected, actual):
    status = "PASS" if expected == actual else "FAIL"
    print(f"  {label}")
    print(f"    expected: {expected}")
    print(f"    actual:   {actual}")
    print(f"    {status}")


# Each check uses its own objects so one check cannot affect another.

print("CHECK 1: CousinLift works inside compare() (duck typing)")
lift = CousinLift("Moris")
compare([lift], 5)  # Prints describe() and the quote.
show("is it a Transport subclass?", False, isinstance(lift, Transport))

print("\nCHECK 2 (normal case): Amina takes the lift with money in her purse")
amina = Journey("Amina", 5000)
result = amina.travel(CousinLift("Moris"), 5)
show("message", "Amina travels by Moris: UGX 0.", result)
show("money left", 5000, amina.purse.balance)  # Free means nothing is spent.
show("completed legs", 1, amina.completed_legs)

print("\nCHECK 3 (boundary case): Peter has UGX 0 and can still take the lift")
peter = Journey("Peter", 0)
result = peter.travel(CousinLift("Moris"), 3)
show("message", "Peter travels by Moris: UGX 0.", result)
show("money left", 0, peter.purse.balance)
show("completed legs", 1, peter.completed_legs)

print("\nCHECK 4 (refused case): distance 0 is not a valid trip")
malish = Journey("Malish", 3000)
result = malish.travel(CousinLift("Moris"), 0)
show("message", "Distance must be positive. No trip started.", result)
show("money left", 3000, malish.purse.balance)  # Nothing changed.
show("completed legs", 0, malish.completed_legs)  # Refused trip not counted.


