import re

def check_password_strength(password):
    strength_points = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength_points += 1
    else:
        feedback.append("🔸 Password should be at least 8 characters long.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength_points += 1
    else:
        feedback.append("🔸 Add lowercase letters (a-z).")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength_points += 1
    else:
        feedback.append("🔸 Add uppercase letters (A-Z).")

    # Check for digits
    if re.search(r"[0-9]", password):
        strength_points += 1
    else:
        feedback.append("🔸 Add digits (0-9).")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_points += 1
    else:
        feedback.append("🔸 Add special characters (e.g., @, #, $, %, !).")

    # Determine strength level
    if strength_points == 5:
        strength = "🔒 Very Strong"
    elif strength_points == 4:
        strength = "✅ Strong"
    elif strength_points == 3:
        strength = "⚠️ Moderate"
    else:
        strength = "❌ Weak"

    return strength, feedback


def main():
    print("=== Password Strength Checker ===")
    user_password = input("Enter your password: ")
    strength, tips = check_password_strength(user_password)

    print(f"\nPassword Strength: {strength}")
    if tips:
        print("Suggestions to improve:")
        for tip in tips:
            print(tip)

if __name__ == "__main__":
    main()

