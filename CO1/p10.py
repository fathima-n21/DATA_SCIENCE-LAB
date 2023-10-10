import re
def is_valid(password):

    if len(password)<6:
        return False
    if not re.search(r'[a-z]',password):
        return False
    if not re.search(r'[A-Z]',password):
        return False
    if not re.search(r'[0-9]',password):
        return False
    if not re.search(r'[$#@]',password):
        return False
    return True
password=input("Enter password")
if is_valid(password):
    print("valid")
else:
    print("Invalid")