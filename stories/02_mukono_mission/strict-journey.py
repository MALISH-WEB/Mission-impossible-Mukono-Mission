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

