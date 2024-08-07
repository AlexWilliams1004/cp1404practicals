from prac_09.taxi import Taxi


def main():
    """Create new taxi object."""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(f"{my_taxi}\nCurrent fare: ${my_taxi.get_fare():.2f}")

    my_taxi.start_fare()
    my_taxi.drive(100)
    print(f"{my_taxi}\nCurrent fare: ${my_taxi.get_fare():.2f}")


if __name__ == "__main__":
    main()
