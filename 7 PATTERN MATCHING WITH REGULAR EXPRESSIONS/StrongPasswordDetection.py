import re

def is_strong_password(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False
    
    # Check if the password contains at least one uppercase letter, one lowercase letter, and one digit
    has_uppercase = re.search(r'[A-Z]', password) is not None
    has_lowercase = re.search(r'[a-z]', password) is not None
    has_digit = re.search(r'\d', password) is not None
    
    return has_uppercase and has_lowercase and has_digit

# Test the function with different passwords
passwords = ["Password123", "password", "PASSWORD", "pass123", "Pass", "12345678", "PassWord!"]
for pwd in passwords:
    print(f"{pwd}: {is_strong_password(pwd)}")