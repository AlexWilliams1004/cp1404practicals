"""
Score - CP1404/CP5632 Practicals

    - Alex Williams 16.08.2024 -

"""

import random


def main():
    """Main function."""
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)
    random_score = random.randint(1, 100)
    random_result = determine_result(random_score)
    print(random_result)


def determine_result(score):
    """Determine result from score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Pass"
    else:
        return "Excellent"


main()
