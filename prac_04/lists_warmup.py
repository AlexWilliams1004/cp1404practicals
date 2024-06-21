"""
CP1401 Practical 4 - Lists Warmup
Alex Williams
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] = 3
# numbers[-1] = 2
# numbers[3] = 1
# numbers[:-1] = 3, 1, 4, 1, 5, 9
# numbers[3:4] = 1
# 5 in numbers = True
# 7 in numbers = False
# "3" in numbers = False
# numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers[0] = "ten"
numbers[-1] = 1
print(numbers[2:])
value = 9
if value in numbers:
    print(f"{value} is an element of numbers")
