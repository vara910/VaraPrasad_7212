# Password Strength Checker
# - Develop a program to check the strength of a password:
# - Criteria: At least 8 characters, includes uppercase, lowercase, digits, and special
# characters.

def check_password_strength(password):
    if len(password) < 8:
        return "Password is too short"
    if password.islower() or password.isupper() or password.isdigit() or password.isalpha():
        return "Password must include the combination of uppercase, lowercase, digits, and special characters"
    return "Password is strong"
password = input("Enter a password to check: ")
print(check_password_strength(password))