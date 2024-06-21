"""
CP1404 Practical 4 - Quick Picks
Alex Williams
"""

import random

NUMBERS_IN_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    number_of_quick_picks = int(input("Number of Quick Picks: "))
    for i in range(number_of_quick_picks):
        quick_pick = generate_quick_pick()
        print(format_quick_pick(quick_pick))


def generate_quick_pick():
    quick_pick = random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUMBERS_IN_PICK)
    quick_pick.sort()
    return quick_pick


def format_quick_pick(quick_pick):
    return ' '.join(f"{number:2}" for number in quick_pick)


main()
