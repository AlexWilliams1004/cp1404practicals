"""
Shop Calculator - CP1404 Practicals

This program allows the user to enter the number of items and
the price of each different item. Then the program computes and
displays the total price of those items. If the total price
is over $100, then a 10% discount is applied to that total
before the amount is displayed on the screen.

    - Alex Williams 16.08.2024 -

"""
total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number")
    number_of_items = int(input("Number of items: "))
for item in range(number_of_items):
    item_price = float(input("Item price: "))
    total_price += item_price
if total_price > 100:
    total_price *= 0.9
print(f"Total price for the {number_of_items} items is ${total_price:.2f}")
