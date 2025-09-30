import re


def strong_password(password: str) -> bool:
    """
    Check if the password is strong.

    A strong password must:
    - Be at least 8 characters long
    - Contain at least one lowercase letter
    - Contain at least one uppercase letter
    - Contain at least one digit
    - Contain at least one special character (@, #, $, %, &, !)

    Returns:
        bool: True if password is strong, False otherwise
    """
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%&!])\S{8,}$"
    return bool(re.match(pattern, password))


tests = ["Password1!", "Pass word1!", "Password1!extraTEXT", "Pass1!"]

for test in tests:
    print(test, "->", strong_password(test))

