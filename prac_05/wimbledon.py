"""
CP1404/CP5632 Practical 5
Wimbledon
Alex Williams

Estimate: 30 minutes
Actual: 45
"""


def main():
    filename = "wimbledon.csv"
    with open(filename, "r", encoding="utf-8-sig") as file:
        lines = file.readlines()
    data = []
    for line in lines[1:]:  # Skip the header
        champion_record = [item.strip() for item in line.strip().split(',')]
        data.append(champion_record)
    champions_count = count_champions_wins(data)
    countries = get_champion_countries(data)

    display_results(champions_count, countries)


def count_champions_wins(data):
    """Count the number of wins for each champion."""
    champion_to_win = {}
    for line in data:
        champion = line[2]
        if champion in champion_to_win:
            champion_to_win[champion] += 1
        else:
            champion_to_win[champion] = 1
    return champion_to_win


def get_champion_countries(data):
    """Get the set of countries of champions."""
    countries = {row[1] for row in data}
    return sorted(countries)


def display_results(champions_count, countries):
    """Display the results."""
    print("Wimbledon Champions:")
    for champion, count in champions_count.items():
        print(f"{champion} {count}")

    winning_countries = ", ".join(countries)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(winning_countries)


main()
