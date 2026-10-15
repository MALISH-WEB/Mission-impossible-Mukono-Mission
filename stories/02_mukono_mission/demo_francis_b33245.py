"""
Extension 1 demo: Student shuttle.
Author: Wagonda Francis Precious B33245.

Run from the main repository folder:
  Windows:        py -3 stories/02_mukono_mission/demo_francis_b33245.py
"""
from story import Boda, Journey, Shuttle, compare

print("=== Extension 1: Student shuttle ===")

# Check 1: compare() can use the Shuttle without any change to compare().
print("\nCheck 1: compare() with a boda and the shuttle, distance 3")
compare([Boda("Kato"), Shuttle("Campus shuttle")], 3)
print("Expected: boda UGX 3,000 and shuttle UGX 1,500")

# Check 2 (normal case): Amina can afford the shuttle.
print("\nCheck 2 (normal): Amina has UGX 5,000 and takes the shuttle")
amina = Journey("Amina", 5000)
print(amina.travel(Shuttle("Campus shuttle"), 3))
print("Expected: money left 3500, legs 1")
print(f"Actual:   money left {amina.purse.balance}, legs {amina.completed_legs}")

# Check 3 (refused case): Peter cannot afford the shuttle.
print("\nCheck 3 (refused): Peter has only UGX 1,000")
peter = Journey("Peter", 1000)
print(peter.travel(Shuttle("Campus shuttle"), 3))
print("Expected: refused, money left 1000, legs 0")
print(f"Actual:   money left {peter.purse.balance}, legs {peter.completed_legs}")

# Check 4 (boundary case): a distance of 0 starts no trip.
print("\nCheck 4 (boundary): Brian has UGX 5,000 and the distance is 0")
brian = Journey("Brian", 5000)
print(brian.travel(Shuttle("Campus shuttle"), 0))
print("Expected: no trip, money left 5000, legs 0")
print(f"Actual:   money left {brian.purse.balance}, legs {brian.completed_legs}")
