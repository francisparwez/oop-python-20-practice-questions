# 17. Static Method — Validate Email 📧
# Create a User class with:
#     name
#     email
# Create a static method:
#     is_valid_email(email)
# It should return True if the email contains:
#     @
#     .
# Otherwise return False .
# Example:
#     User.is_valid_email("ali@gmail.com")
# Output:
#     True
# Practice: @staticmethod

import re

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    @staticmethod
    def is_valid_email(email):
        pattern = r"^[^@]+@[^@]+\.[^@]+$"
        return bool(re.match(pattern, email))
    

if __name__ == '__main__':
    email1 = "ali@gmail.com"
    email2 = "ali.gmail.com"
    email3 = "aligmailcom"
    
    print(User.is_valid_email(email1))
    print(User.is_valid_email(email2))
    print(User.is_valid_email(email3))
    print(User.is_valid_email("ali@."))