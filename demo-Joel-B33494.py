#Demonstrating Extension 4:Cheapest ride.

from story import WalkWithFriend, Journey, compare

def cheapest(options, distance):
    if distance <= 0:
        raise ValueError("Distance must be positive.")

    if not options:
        return None

    cheapest_option = options[0]
    lowest_fare = cheapest_option.quote_fare(distance)

    for option in options[1:]:
        fare = option.quote_fare(distance)

        if fare < lowest_fare:
            cheapest_option = option
            lowest_fare = fare

    return cheapest_option


def main():
#Tested in main() function to find the cheapest transport option for a distance of 3 km.
    options = [WalkWithFriend()]
    best = cheapest(options, 3)
    if best is not None:
        print(f"Cheapest option: {best.name}")
        print(f"Fare: UGX {best.quote_fare(3):,}")
    else:
        print("No transport options available.")

    
#Tested in main() function to find the cheapest transport option for a distance of 0 km.
    options = [WalkWithFriend()]
    best = cheapest(options, 0)
    if best is not None:
        print(f"Cheapest option: {best.name}")
        print(f"Fare: UGX {best.quote_fare(0):,}")
    else:
        print("No transport options available.")
            
            
if __name__ == "__main__":
    main()

