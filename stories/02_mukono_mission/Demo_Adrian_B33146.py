"""Demonstrate Extension 2: adding money to a transport purse."""
from story import TripPurse


def main():
	# A positive top-up adds to the purse and reports success.
	purse = TripPurse(2000)
	result = purse.top_up(1500)
	print("Positive top-up: expected True and balance UGX 3,500")
	print(f"Actual: {result} and balance UGX {purse.balance:,}")

	# Zero is rejected, so the balance stays unchanged.
	zero_purse = TripPurse(2000)
	result = zero_purse.top_up(0)
	print("Zero top-up: expected False and balance UGX 2,000")
	print(f"Actual: {result} and balance UGX {zero_purse.balance:,}")

	# Negative amounts are rejected without reducing the balance.
	negative_purse = TripPurse(2000)
	result = negative_purse.top_up(-500)
	print("Negative top-up: expected False and balance UGX 2,000")
	print(f"Actual: {result} and balance UGX {negative_purse.balance:,}")


if __name__ == "__main__":
	main()
