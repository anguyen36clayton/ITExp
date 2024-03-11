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
    grade = 0

    # Check for lowercase, uppercase, numbers, and symbols
    has_lower = 1 if re.search(r"[a-z]", password) else 0
    has_upper = 1 if re.search(r"[A-Z]", password) else 0
    has_digit = 1 if re.search(r"\d", password) else 0
    has_special = 1 if re.search(r"[!@#$%^&*()_+\-=[\]{};':\"\\|,.<>/?]", password) else 0  # Updated pattern for special characters

    # Add 20% for each criterion
    grade += has_lower * 20
    grade += has_upper * 20
    grade += has_digit * 20
    grade += has_special * 20

    # Additional 20% if length >= 8
    if len(password) >= 8:
        grade += 20

    # Ensure the grade doesn't exceed 100%
    grade = min(grade, 100)

    return f"Password Grade: {grade}%"

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
