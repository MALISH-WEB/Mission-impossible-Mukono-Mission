


from story import Boda, Taxi, StudentBoda
from story import CheerfulStudentBoda, WalkWithFriend
from story import Journey, TripPurse


class FareMoney:
    def __init__(self, amount):
        if isinstance(amount, bool) or not isinstance(amount, int):
            raise TypeError("Amount must be a whole number.")

        if amount < 0:
            raise ValueError("Amount cannot be negative.")

        self.__amount = amount

    @property
    def amount(self):
        return self.__amount

    def __str__(self):
        return f"UGX {self.amount:,}"

    def __repr__(self):
        return f"FareMoney({self.amount})"

    def __eq__(self, other):
        if not isinstance(other, FareMoney):
            return NotImplemented
        return self.amount == other.amount

    def __add__(self, other):
        if not isinstance(other, FareMoney):
            return NotImplemented
        return FareMoney(self.amount + other.amount)


class BodaChoice:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km

    def quote_fare(self, distance):
        return FareMoney(self.rate_per_km * distance)


class TaxiChoice:
    def __init__(self, base_fare, rate_per_km):
        self.base_fare = base_fare
        self.rate_per_km = rate_per_km

    def quote_fare(self, distance):
        return FareMoney(
            self.base_fare + self.rate_per_km * distance
        )



def validate_distance(distance):
    if isinstance(distance, bool) or not isinstance(distance, int):
        raise TypeError("Distance must be a whole number.")

    if distance <= 0:
        raise ValueError("Distance must be positive.")


def preview_total(choices, distance):
    validate_distance(distance)

    total = FareMoney(0)

    for choice in choices:
        quote = choice.quote_fare(distance)

        if not isinstance(quote, FareMoney):
            raise TypeError(
                "Each choice must return a FareMoney value."
            )

        total = total + quote

    return total



# Test the money class
fare1 = FareMoney(6000)
fare2 = FareMoney(8000)

print("First fare:", fare1)
print("Combined fares:", fare1 + fare2)

# Compare transport choices
choices = [
    BodaChoice(rate_per_km=1000),
    TaxiChoice(base_fare=2000, rate_per_km=1500),
]

print("Total preview:", preview_total(choices, 3))
