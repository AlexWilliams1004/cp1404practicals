"""
files
"""

# Program 1
out_file = open("name.txt", 'w')
name = input("name: ")
print(name, file=out_file)
out_file.close()

# Program 2
in_file = open("name.txt", 'r')
name = in_file.read().strip()
in_file.close()
print(f"Your name is {name}")

# Program 3
with open("numbers.txt", 'r') as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
print(first_number + second_number)

# Program 4
with open("numbers.txt", 'r') as in_file:
    total = 0
    for line in in_file:
        number = int(line)
        total += number
    print(total)
