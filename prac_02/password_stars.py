"""
Password Stars - CP1404 Practicals

    - Alex Williams 16.08.2024 -

"""


def main():
    """Main function."""
    password_length = 10
    password = get_valid_password(password_length)
    print_password(password)


def get_valid_password(password_length):
    """Get a valid password length."""
    password = input("Enter your password: ")
    while len(password) < password_length:
        print(f"Password must be at least {password_length} long.")
        password = input("Enter your password: ")
    return password


def print_password(password):
    """Print stars of password length."""
    print(f"{'*' * len(password)}")


main()
