import re

def password_strength(password):
    if len(password) < 8:
        return "Password is too short"
    
    has_lowercase = any(char.islower() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_digits = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()_+}{|\":<>?,.';\\[\\]" for char in password)
    
    complexity = sum([has_lowercase, has_uppercase, has_digits, has_special])
    
    if complexity < 4:
        return "Weak password: lacks complexity"
    
    common_patterns = [r'123', r'abc', r'password', r'qwerty', r'111', r'admin', r'master']
    for pattern in common_patterns:
        if re.search(pattern, password, re.IGNORECASE):
            return "Weak password: contains common pattern"
    
    return "Strong password: meets criteria"

password = input("Enter the password: ")
print(password_strength(password))
