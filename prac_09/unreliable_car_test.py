"""
Unreliable Car Test - CP1404 Practical 9
Alex Williams
"""

from unreliable_car import UnreliableCar


def main():
    """Create an unreliable car object with 50% reliability."""
    unreliable_car = UnreliableCar("Hilux", 100, 50)
    for i in range(10):
        distance_driven = unreliable_car.drive(20)
        print(
            f"Attempt {i + 1}: Drove {distance_driven}km, {unreliable_car.odometer}, Fuel left: {unreliable_car.fuel}")


if __name__ == "__main__":
    main()
