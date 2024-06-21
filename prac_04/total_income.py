"""
CP1404/CP5632 Practical
Updated cumulative total income program
Alex Williams
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_report_header()
    report_totals = add_report_total(incomes, number_of_months)
    for report_total in report_totals:
        print(report_total)


def print_report_header():
    print("\nIncome Report\n-------------")


def add_report_total(incomes, number_of_months):
    totals = []
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        totals.append("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))
    return totals


main()
