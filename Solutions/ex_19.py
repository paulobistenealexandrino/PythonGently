# Exercise #19: Password Generator
import random
random.seed(42)

def generatePassword(length=12) -> str:
    import random

    if length < 12:
        length = 12       

    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = lowercase_letters.upper()
    numbers = '0123456789'
    special_characters = '~!@#$%^&*()_+'
    all_characters = lowercase_letters + uppercase_letters + numbers + special_characters    

    password_list = []
    password_list.append(lowercase_letters[random.randint(0, len(lowercase_letters) - 1)])
    password_list.append(uppercase_letters[random.randint(0, len(uppercase_letters) - 1)])
    password_list.append(numbers[random.randint(0, len(numbers) - 1)])
    password_list.append(special_characters[random.randint(0, len(special_characters) - 1)])
    for i in range(4, length):
        password_list.append(all_characters[random.randint(0, len(all_characters) - 1)])

    random.shuffle(password_list)
    password = ''.join(password_list)    

    return password

# Testing function
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '1234567890'
SPECIAL = '~!@#$%^&*()_+'
pw = generatePassword(14)
assert len(pw) == 14
hasLowercase = False
hasUppercase = False
hasNumber = False
hasSpecial = False
for character in pw:
    if character in LOWER_LETTERS:
        hasLowercase = True
    if character in UPPER_LETTERS:
        hasUppercase = True
    if character in NUMBERS:
        hasNumber = True
    if character in SPECIAL:
        hasSpecial = True
assert hasLowercase and hasUppercase and hasNumber and hasSpecial