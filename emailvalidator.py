import re

def valid_email(email: str) -> bool:
    email_regex = r'^[a-zA-Z0-9._]+@[a-z]+\.[a-z]{2,}$'
    if re.match(email_regex, email):
        return True
    else:
        return False

email = input("Enter email: ")
if valid_email(email=email):
    print("Valid Email")
else:
    print("Invalid Email")
