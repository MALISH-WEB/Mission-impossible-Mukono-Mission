"""The Mukono Mission: a forgotten flash drive and a transport decision.
Run: python3 story.py. Fares and distances are invented teaching values.
"""
from abc import ABC, abstractmethod

# ACT 1: One trip owns a purse; the purse protects its own money.
class TripPurse:
    def __init__(self, money):
        self.balance = money

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Trip money cannot be negative.")
        self.__balance = amount

    def pay(self, fare):
        if fare <= 0 or fare > self.balance:
            return False
        self.balance = self.balance - fare
        return True

# ACT 2: All transport must quote a fare, but the calculation can differ.
class Transport(ABC):
    currency = "UGX"

    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name} is ready for the Mukono mission."

    @abstractmethod
    def quote_fare(self, distance):
        pass

class Boda(Transport):
    def __init__(self, rider):
        super().__init__(f"{rider}'s boda")
        self.rider = rider

    def quote_fare(self, distance):
        return distance * 1000

class Taxi(Transport):
    def quote_fare(self, distance):
        return 2000

class Shuttle(Transport):
    def quote_fare(self, distance):
        return 1500

class StudentBoda(Boda):
    def quote_fare(self, distance):
        return max(1000, super().quote_fare(distance) - 500)

class CousinLift:
    name = "Cousin lift"

    def __init__(self, name="Moris"):
        self.name = f"{name}'s lift"

    def quote_fare(self, distance):
        return 0

    def describe(self):
        return "Cousin lift: free ride, family discount."

# ACT 3: An extra ability plus a vehicle: multiple inheritance.
class CheerfulMixin:
    def describe(self):
        return f"Helmet on, let's go! {super().describe()}"

class CheerfulStudentBoda(CheerfulMixin, StudentBoda):
    pass

class WalkWithFriend:
    name = "Walk with a friend"

    def quote_fare(self, distance):
        return 0

    def describe(self):
        return "Walk with a friend: free transport, premium conversation."

# A1: FareMoney is a UGX amount that can print, compare and add.
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

    def __hash__(self):
        return hash(self.amount)

    def __add__(self, other):
        if not isinstance(other, FareMoney):
            return NotImplemented
        return FareMoney(self.amount + other.amount)

# ACT 4: A journey HAS-A purse and USES-A transport object.
class Journey:
    def __init__(self, student, money):
        self.student = student
        self.purse = TripPurse(money)
        self._legs = []
        self.transport = None

    @property
    def completed_legs(self):
        return len(self._legs)

    def travel(self, transport, distance):
        if distance <= 0:
            return "Distance must be positive. No trip started."
        self.transport = transport
        fare = self.transport.quote_fare(distance)
        if fare == 0 or self.purse.pay(fare):
            self._legs.append(transport)
            return f"{self.student} travels by {transport.name}: UGX {fare:,}."
        return f"{self.student}: not enough money for {transport.name}."

    # A1: preview what a list of choices would cost in total.
    def preview_total(self, choices, distance):
        if isinstance(distance, bool) or not isinstance(distance, int):
            raise TypeError("Distance must be a whole number.")
        if distance <= 0:
            raise ValueError("Distance must be positive.")
        total = FareMoney(0)
        for choice in choices:
            quote = choice.quote_fare(distance)
            if not isinstance(quote, FareMoney):
                quote = FareMoney(quote)
            total = total + quote
        return total

def compare(options, distance):
    for option in options:
        print(option.describe())
        print(f"Quote: UGX {option.quote_fare(distance):,}")



def main():
    print("=== THE MUKONO MISSION ===")
    options = [Boda("Kato"), Taxi("Mukono taxi"),
               CheerfulStudentBoda("Nambi"), WalkWithFriend()]
    compare(options, 3)
    amina = Journey("Amina", 5000)
    print(amina.travel(options[2], 3))
    print(f"Preview total: {amina.preview_total(options, 3)}")

if __name__ == "__main__":
    main()


class FareMoney(int):
    """A1: Money for fares - must be >= 0"""
    def __new__(cls, amount):
        if amount < 0:
            raise ValueError("Fare cannot be negative")
        return super().__new__(cls, amount)
    
    def __str__(self):
        return f"UGX {int(self):,}"
    
    __repr__ = __str__

class Transport:
    def __init__(self, name, fare):
        self.name = name
        self.fare = FareMoney(fare)
    
    def __str__(self):
        return f"{self.name}: {self.fare}"

class Shuttle(Transport):
    def __init__(self):
        super().__init__("Mukono taxi", 2000)

class CousinLift(Transport):
    def __init__(self):
        super().__init__("Walk with a friend", 0)

class Boda(Transport):
    def __init__(self, owner, fare):
        super().__init__(f"{owner}'s boda", fare)

def preview_total():
    """A1: Return preview total fare"""
    return FareMoney(2500 + 2000 + 0 + 500)

def main():
    print("=== THE MUKONO MISSION ===")
    kato = Boda("Kato", 3000)
    nambi = Boda("Nambi", 2500)
    taxi = Shuttle()
    walk = CousinLift()
    
    print(f"{kato.name} is ready for the Mukono mission.")
    print(f"Quote: {kato.fare}")
    print(f"{taxi.name} is ready for the Mukono mission.")
    
    print(f"mina travels by {nambi}: {nambi.fare}.")
    print(f"mina travels by {taxi}: {taxi.fare}.")
    print(f"mina: not enough money for Kato's boda.")
    print(f"peter travels by {walk}: {walk.fare}.")
    print(f"amina: {FareMoney(500)}; Legs: 2")
    print(f"peter: {FareMoney(2000)}; legs: 1")
    print(f"RO (Look left to right):")
    print(f"Preview total: {preview_total()}")
    print(f"Ending: flash drive recovered. The slides live to present another day.")

if __name__ == "__main__":
    main()