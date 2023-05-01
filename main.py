import secrets
import string

# creates three variables: letters, numbers, and special_chars to refer to the characters available to be in a pwd
letters = string.ascii_letters
numbers = string.digits
special_chars = string.punctuation

# concantenates all legal characters into an alphabet list
alphabet = letters + numbers + special_chars

# determines the length of the password
pwd_length = 12


# generates password meeting pwd constraints: (1) should contain at least one special character, (2) should contain at least two digits
while True:
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))

    if (any(char in special_chars for char in pwd) and sum(char in numbers for char in pwd)>=2):
        break

print(pwd)