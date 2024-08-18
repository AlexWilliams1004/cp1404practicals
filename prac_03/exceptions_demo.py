"""
Exceptions - CP1404 Practicals

Answer the following questions:
1. When will a ValueError occur?
    - In this case, when the inputs are not integers.
2. When will a ZeroDivisionError occur?
    - In this case, when the denominator input is zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    - Yes.

    - Alex Williams 18-08.2024 -

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
