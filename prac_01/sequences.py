"""
Menu Driven Number Sequences - CP1404 Practicals

    - Alex Williams 16.08.2024 -

"""
x = int(input("x: "))
y = int(input("y: "))
menu = """1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)
4. Exit the program"""
print(menu)
choice = input(">>> ")
while choice != "4":
    if choice == "1":
        for i in range(x + x % 2, y + 1, 2):
            print(i, end=' ')
    elif choice == "2":
        if x % 2 != 0:
            for i in range(x, y + 1, 2):
                print(i, end=' ')
        else:
            for i in range(x + 1, y + 1, 2):
                print(i, end=' ')
    else:
        for i in range(x, y + 1):
            print(i ** 2, end=' ')
    print()
    print(menu)
    choice = input(">>> ")
print("Program finished")
