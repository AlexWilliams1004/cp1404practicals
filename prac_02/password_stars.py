def main():
    password_length = 10
    password = get_valid_password(password_length)
    print_password(password)


def print_password(password):
    print(f"{'*' * len(password)}")


def get_valid_password(password_length):
    password = input("Enter your password: ")
    while len(password) < password_length:
        print(f"Password must be at least {password_length} long.")
        password = input("Enter your password: ")
    return password


main()
