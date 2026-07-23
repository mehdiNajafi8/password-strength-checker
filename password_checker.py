"""
Password Strength Checker
A simple beginner project for learning Python + basic security concepts.
"""

import re


def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase letter check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase letter check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Number check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&* etc).")

    # Common weak password check
    common_passwords = ["123456", "password", "qwerty", "111111", "12345678"]
    if password.lower() in common_passwords:
        score = 0
        feedback = ["This is a very common password. Choose something unique."]

    # Rating
    if score >= 6:
        rating = "Strong"
    elif score >= 4:
        rating = "Medium"
    else:
        rating = "Weak"

    return rating, feedback


def main():
    print("=== Password Strength Checker ===")
    password = input("Enter a password to check: ")

    rating, feedback = check_password_strength(password)

    print(f"\nStrength: {rating}")
    if feedback:
        print("Suggestions to improve:")
        for tip in feedback:
            print(f"  - {tip}")
    else:
        print("Great! Your password meets all the basic security criteria.")


if __name__ == "__main__":
    main()
