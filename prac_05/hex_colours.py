"""
CP1404/CP5632 Practical 5
Hexadecimal Colours

Alex Williams
"""

NAME_TO_CODE = {"Black": "#000000", "Brown": "#a52a2a", "White": "#ffffff",
                "Gray": "#bebebe", "Yellow": "#ffff00", "Red": "#ff0000",
                "Green": "#00ff00", "Purple": "#a020f0", "Pink": "#ffc0cb",
                "Blue": "#0000ff"}

name = input("Colour name: ").title()
while name != "":
    try:
        print(f"{name} is {NAME_TO_CODE[name]}")
    except KeyError:
        print("Invalid name")
    name = input("Colour name: ").title()
