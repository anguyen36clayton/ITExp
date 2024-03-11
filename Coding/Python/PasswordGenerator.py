import random
import string
import re

def generate_password():
    """Generates a random password between 8 and 12 characters."""
    characters = string.ascii_letters + string.digits + string.punctuation.replace('~', '').replace('`', '').replace("'", '')
    password_length = random.randint(8, 12)
    
    # Ensure at least one lowercase letter, one uppercase letter, one digit, and one special character
    password = random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice(string.punctuation)
    password += "".join(random.choice(characters) for _ in range(password_length - 4))

    # Shuffle the password to make the order random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def check_password_strength(password):
    """Checks the strength of a password based on common criteria."""

    # Minimum length requirements
    length_grade = 0
    if len(password) >= 8:
        length_grade = 25
    if len(password) >= 12:
        length_grade = 50

    # Check for lowercase, uppercase, numbers, and symbols
    has_lower = re.search(r"[a-z]", password)
    has_upper = re.search(r"[A-Z]", password)
    has_digit = re.search(r"\d", password)
    has_special = re.search(r"[!@#$%^&*()_+\-=[\]{};':\"\\|,.<>/?]", password)  # Updated pattern for special characters

    count = sum(1 for check in [has_lower, has_upper, has_digit, has_special] if check)
    grade = count * 25

    return f"Password Grade: {grade + length_grade}%"

while True:
    choice = input("Do you want to generate a random password? (yes/no): ")
    if choice.lower() == "yes":
        num_passwords = int(input("Enter the number of passwords to create: "))
        for _ in range(num_passwords):
            password = generate_password()
            print("Your random password is:", password)
            result = check_password_strength(password)
            print(result)
        break
    elif choice.lower() == "no":
        print("Okay, exiting.")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
