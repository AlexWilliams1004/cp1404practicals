password_length = 10
password = input("Enter your password: ")
while len(password) < password_length:
    print(f"Password must be at least {password_length} long.")
    password = input("Enter your password: ")
print(f"{'*' * len(password)}")
