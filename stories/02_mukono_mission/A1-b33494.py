from story import FareMoney

class FareMoney:
    def __init__(self, amount):
        # bool is a subclass of int, so reject it explicitly
        if isinstance(amount, bool) or not isinstance(amount, int):
            raise TypeError("Amount must be a whole number.")

        if amount < 0:
            raise ValueError("Amount cannot be negative.")

        self.__amount = amount

    @property
    def amount(self):
        """Read-only amount in UGX."""
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


class Journey:
    def __init__(self):
        self.history = []

    def preview_total(self, choices, distance):
        # Validate before asking any choice for a quote
        if isinstance(distance, bool) or not isinstance(distance, int):
            raise TypeError("Distance must be a whole number.")

        if distance <= 0:
            raise ValueError("Distance must be positive.")

        total = FareMoney(0)

        for choice in choices:
            quote = choice.quote_fare(distance)

            if not isinstance(quote, FareMoney):
                raise TypeError(
                    "Each choice must return a FareMoney value."
                )

            total = total + quote

        return total


# ---------------- DEMONSTRATION ----------------

# Equality and inequality
fare1 = FareMoney(3000)
fare2 = FareMoney(3000)
fare3 = FareMoney(4500)

print("Equal values:", fare1 == fare2)
print("Unequal values:", fare1 == fare3)

# Friendly display versus developer representation
print("Display:", fare1)
print("Representation:", repr(fare1))

# Addition
fare4 = FareMoney(2000)
combined = fare1 + fare4

print("Combined:", combined)
print("First operand unchanged:", fare1)
print("Second operand unchanged:", fare4)

# Unsupported operands
print("Unsupported equality:", fare1 == 3000)

try:
    result = fare1 + 3000
except TypeError as error:
    print("Unsupported addition:", error)

# Invalid construction
for invalid_amount in (-100, 2.5, True):
    try:
        FareMoney(invalid_amount)
    except (TypeError, ValueError) as error:
        print(f"Invalid amount {invalid_amount!r}: {error}")

# Read-only property
try:
    fare1.amount = 5000
except AttributeError as error:
    print("Read-only property:", error)

# Journey preview with different choice types
journey = Journey()
choices = [
    BodaChoice(rate_per_km=1000),
    TaxiChoice(base_fare=2000, rate_per_km=1500),
]

total = journey.preview_total(choices, distance=3)

print("Journey preview:", total)
print("Journey history:", journey.history)

# Empty list
print("Empty preview:", journey.preview_total([], distance=3))

# Reject invalid distance before quoting
try:
    journey.preview_total(choices, distance=0)
except ValueError as error:
    print("Invalid distance:", error)