"""
CP1404/CP5632 Practical 5
Emails
Alex Williams

Estimate: 20 minutes
Actual: 30
"""


def main():
    """Store email addresses and names in a dictionary."""
    email_to_name = {}

    email = input("Email Address: ").lower()
    while email != "":
        name = display_name(email)
        confirmation = input(f"Is your name {name}? [Y/n] ")
        if confirmation != "Y" and confirmation != "":
            name = input("Name: ").title()

        email_to_name[email] = name  # add key-value pair to dictionary
        email = input("Email Address: ").lower()

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def display_name(email):
    """Display email address's corresponding name."""
    name = email.split('@')[0]
    name = name.replace('.', ' ')
    name = name.title()
    return name


main()
