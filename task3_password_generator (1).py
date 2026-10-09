"""
CodeSoft Internship - Task 3: Password Generator
----------------------------------------------------
"""

import random
import string


def get_length():
    """Ask the user for a valid password length."""
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 4:
                print("Please choose a length of at least 4 for a secure password.")
                continue
            return length
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_complexity():
    """Ask the user which character sets to include."""
    print("\nSelect complexity options (y/n for each):")
    use_upper = input("Include uppercase letters (A-Z)? (y/n): ").strip().lower() == "y"
    use_lower = input("Include lowercase letters (a-z)? (y/n): ").strip().lower() == "y"
    use_digits = input("Include numbers (0-9)? (y/n): ").strip().lower() == "y"
    use_symbols = input("Include symbols (!@#$%^&*)? (y/n): ").strip().lower() == "y"

    # If the user selects nothing, default to letters + digits
    if not any([use_upper, use_lower, use_digits, use_symbols]):
        print("No options selected. Defaulting to letters and numbers.")
        use_upper = use_lower = use_digits = True

    return use_upper, use_lower, use_digits, use_symbols


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    """Build a random password from the selected character pools."""
    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += "!@#$%^&*()-_=+"

    password = "".join(random.choice(char_pool) for _ in range(length))
    return password


def main():
    print("========== PASSWORD GENERATOR ==========")

    while True:
        length = get_length()
        use_upper, use_lower, use_digits, use_symbols = get_complexity()

        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        print(f"\nYour generated password: {password}\n")

        again = input("Generate another password? (y/n): ").strip().lower()
        if again != "y":
            print("Thank you for using the Password Generator. Stay secure!")
            break


if __name__ == "__main__":
    main()
