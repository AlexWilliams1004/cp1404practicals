"""
Loops - CP1404 Practicals

    - Alex Williams 16.08.2024 -

"""
# a
for i in range(0, 101, 10):
    print(i, end=' ')

# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c
number = int(input("Number: "))
for n in range(number):
    print("*", end='')
print()

# d
number = int(input("Number: "))
for i in range(number):
    for j in range(i + 1):
        print("*", end='')
    print()
