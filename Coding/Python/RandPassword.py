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
    if len(password) < 8:
        return "Password is too short. It should be at least 8 characters long."

    # Check for lowercase, uppercase, numbers, and symbols
    has_lower = re.search(r"[a-z]", password)
    has_upper = re.search(r"[A-Z]", password)
    has_digit = re.search(r"\d", password)
    has_special = re.search(r"[!@#$%^&*()_+\-=[\]{};':\"\\|,.<>/?]", password)  # Updated pattern for special characters

    if not has_lower or not has_upper or not has_digit or not has_special:
        return "Password should contain a mix of lowercase, uppercase, numbers, and symbols."

    # Check for common patterns (optional)
    if re.search(r"[\w]{3,}\d+[\w]{3,}", password):  # Letters and numbers in sequence
        return "Password might be too predictable. Avoid common patterns."

    # Password meets strength requirements
    return "Password is strong!"

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

