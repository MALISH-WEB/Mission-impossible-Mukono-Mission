"""A2 demo: errors the Mukono Mission can explain.

Malish Emmanuel Abui
B33239
Run from the repository root with:

    python3 stories/02_mukono_mission/demo_a2_emmanuel_b33239.py
"""

import os
import sys

# Allows this file to work when run from the repository root.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from story import (  # noqa: E402
    Boda,
    Journey,
    JourneyChoiceError,
    JourneyRequestError,
    JourneyResourceError,
    StrictJourney,
    WalkWithFriend,
)


class NegativeFareChoice:
    """Fake choice used to test an invalid negative fare."""

    name = "Invalid negative-fare choice"

    def describe(self):
        return "A fake choice that returns an invalid negative fare."

    def quote_fare(self, distance):
        return -500


def show_state(label, journey, expected_money, expected_legs):
    """Print and check that a failed attempt did not change the Journey."""
    actual_money = journey.purse.balance
    actual_legs = journey.completed_legs
    status = (
        "PASS"
        if actual_money == expected_money and actual_legs == expected_legs
        else "FAIL"
    )

    print(f"[{status}] {label}")
    print(f"  expected money: {expected_money}")
    print(f"  actual money:   {actual_money}")
    print(f"  expected legs:  {expected_legs}")
    print(f"  actual legs:    {actual_legs}")


def attempt(label, strict_journey, choice, distance):
    """Run one request and display a friendly result."""
    print(f"\n--- {label} ---")

    try:
        result = strict_journey.safe_travel(choice, distance)
        print(f"Success: {result}")
    except JourneyChoiceError as error:
        print(f"Choice problem: {error}")
    except JourneyRequestError as error:
        print(f"Request problem: {error}")
    except JourneyResourceError as error:
        print(f"Resource problem: {error}")
    finally:
        print("Attempt complete.")


def main():
    # Each failed check uses a separate Journey so the state is easy to verify.

    print("=== A2: Errors the Mukono Mission can explain ===")

    print("\nCHECK 1: Missing choice")
    missing_choice_journey = Journey("Amina", 5000)
    missing_choice = StrictJourney(missing_choice_journey)

    attempt("None is not a valid choice", missing_choice, None, 3)
    show_state(
        "missing choice leaves the Journey unchanged",
        missing_choice_journey,
        expected_money=5000,
        expected_legs=0,
    )

    print("\nCHECK 2: Invalid distance")
    invalid_distance_journey = Journey("Brian", 5000)
    invalid_distance = StrictJourney(invalid_distance_journey)

    attempt(
        "zero distance is rejected before travel",
        invalid_distance,
        WalkWithFriend(),
        0,
    )
    show_state(
        "invalid distance leaves the Journey unchanged",
        invalid_distance_journey,
        expected_money=5000,
        expected_legs=0,
    )

    print("\nCHECK 3: Invalid negative fare")
    negative_fare_journey = Journey("Chris", 5000)
    negative_fare = StrictJourney(negative_fare_journey)

    attempt(
        "a negative calculated fare is rejected",
        negative_fare,
        NegativeFareChoice(),
        3,
    )
    show_state(
        "negative fare leaves the Journey unchanged",
        negative_fare_journey,
        expected_money=5000,
        expected_legs=0,
    )

    print("\nCHECK 4: Not enough money")
    poor_journey = Journey("Diana", 1000)
    poor_traveller = StrictJourney(poor_journey)

    attempt(
        "a valid request that costs too much is refused",
        poor_traveller,
        Boda("Kato"),
        3,
    )
    show_state(
        "unaffordable request leaves the Journey unchanged",
        poor_journey,
        expected_money=1000,
        expected_legs=0,
    )

    print("\nCHECK 5: Valid affordable request")
    successful_journey = Journey("Amina", 5000)
    successful_traveller = StrictJourney(successful_journey)

    attempt(
        "an affordable boda trip succeeds",
        successful_traveller,
        Boda("Kato"),
        3,
    )
    show_state(
        "successful request spends money and records one leg",
        successful_journey,
        expected_money=2000,
        expected_legs=1,
    )

    print("\nCHECK 6: A zero-cost choice is valid")
    free_journey = Journey("Peter", 0)
    free_traveller = StrictJourney(free_journey)

    attempt(
        "a free walking trip is not confused with a missing choice",
        free_traveller,
        WalkWithFriend(),
        3,
    )
    show_state(
        "zero-cost choice succeeds without spending money",
        free_journey,
        expected_money=0,
        expected_legs=1,
    )


if __name__ == "__main__":
    main()