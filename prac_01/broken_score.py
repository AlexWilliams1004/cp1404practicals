"""
CP1404/CP5632 - Practical
Broken program to determine score status

    - Alex Williams 16.08.2024 -

"""

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score < 50:
    print("Bad")
elif score < 90:
    print("Pass")
else:
    print("Excellent")
