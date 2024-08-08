"""
Silver Service Taxi Test - CP1404 Practical 9
Alex Williams
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Create a new silver service taxi object with a fanciness of 2."""
    fancy_taxi = SilverServiceTaxi("Stretch Hummer", 200, 2)
    fancy_taxi.drive(18)
    print(f"{fancy_taxi}\nCurrent fare: ${fancy_taxi.get_fare():.2f}")
    assert fancy_taxi.get_fare() == 48.78, "The fare should be 48.78 for an 18km trip with fanciness of 2."


if __name__ == '__main__':
    main()
