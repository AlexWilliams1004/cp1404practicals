"""
Score menu program
"""

MENU = "(G)et a valid score (mush be between 0-100 inclusive)\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score("Score: ", 0, 100)
            print(score)
        elif choice == "P":
            result = determine_result(score)
            print(result)
        else:
            show_stars(score)
        print(MENU)
        choice = input(">>>").upper()
    print("Bye!")


def get_valid_score(prompt, low, high):
    score = int(input(prompt))
    while score < low or score > high:
        print("invalid score")
        score = int(input(prompt))
    return score


def determine_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    print(f"{'*' * score}")


main()
