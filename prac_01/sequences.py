"""
Menu Driven Number Sequences - CP1404 Practicals

This program will ask the user for integer inputs that will
be stored in x and y variables, then display a menu that
will allow the user to choose from the following options:

1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)
4. Exit the program

    - Alex Williams 16.08.2024 -

"""
MENU = """1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)
4. Exit the program"""


def main():
    """Main function."""
    x = int(input("x: "))
    y = int(input("y: "))
    print(MENU)
    choice = input(">>> ")
    while choice != "4":
        if choice == "1":
            display_even_numbers(x, y)
        elif choice == "2":
            display_odd_numbers(x, y)
        else:
            display_numbers_squared(x, y)
        print()
        print(MENU)
        choice = input(">>> ")
    print("Program finished")


def display_even_numbers(x, y):
    """Display the even numbers between x and y."""
    for i in range(x + x % 2, y + 1, 2):
        print(i, end=' ')


def display_odd_numbers(x, y):
    """Display the odd numbers between x and y."""
    if x % 2 != 0:
        for i in range(x, y + 1, 2):
            print(i, end=' ')
    else:
        for i in range(x + 1, y + 1, 2):
            print(i, end=' ')


def display_numbers_squared(x, y):
    """Display all the numbers squared."""
    for i in range(x, y + 1):
        print(i ** 2, end=' ')


if __name__ == '__main__':
    main()
