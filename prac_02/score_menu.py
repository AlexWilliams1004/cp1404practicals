"""
Score menu program - CP1404 Practicals
This is the updated version of the score
program with the menu

    - Alex Williams 16.08.2024 -

"""

MENU = """(G)et a valid score (mush be between 0-100 inclusive)
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Main program."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score("Score: ", 0, 100)
            print(score)
        elif choice == "P":
            result = determine_result(score)
            print(result)
        else:
            print_stars(score)
        print(MENU)
        choice = input(">>> ").upper()
    print("Bye!")


def get_valid_score(prompt, low, high):
    """Get valid score."""
    score = int(input(prompt))
    while score < low or score > high:
        print("invalid score")
        score = int(input(prompt))
    return score


def determine_result(score):
    """Determine result from score."""
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Pass"
    else:
        return "Excellent"


def print_stars(score):
    """Print score length of stars."""
    print(f"{'*' * score}")


main()
