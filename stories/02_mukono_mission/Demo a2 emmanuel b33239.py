# Demo for A2: Errors the story can explain (StrictJourney.safe_travel)
# Emmanuel, access number B33239
from story import (Boda, Taxi, WalkWithFriend, StrictJourney,
                   JourneyChoiceError, JourneyRequestError,
                   JourneyResourceError)


def attempt(journey, choice, distance, expected):
    print(f"\nExpected: {expected}")
    try:
        print("Actual:  ", journey.safe_travel(choice, distance))
    except JourneyChoiceError as error:
        print("Actual:   Choice problem -", error)
    except JourneyRequestError as error:
        print("Actual:   Request problem -", error)
    except JourneyResourceError as error:
        print("Actual:   Not enough money -", error)
    finally:
        print(f"Attempt finished. UGX {journey.purse.balance:,} left, "
              f"{journey.completed_legs} leg(s).")


class BrokenQuote:  # Tiny fake choice that quotes a negative fare.
    name = "Broken quote"

    def quote_fare(self, distance):
        return -500


amina = StrictJourney("Amina", 5000)
attempt(amina, Taxi("Mukono taxi"), 3, "success, UGX 3,000 left, 1 leg")
attempt(amina, None, 3, "choice problem, nothing changes")
attempt(amina, Taxi("Mukono taxi"), 0, "request problem, nothing changes")
attempt(amina, BrokenQuote(), 3, "request problem, nothing changes")
attempt(amina, Boda("Kato"), 4, "not enough money, nothing changes")
attempt(amina, WalkWithFriend(), 3, "success (free), still UGX 3,000, 2 legs")