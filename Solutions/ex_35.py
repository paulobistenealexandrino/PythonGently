# Exercise #35: Title Case

def getTitleCase(text: str) -> str:
    """Convert a string to title case
    
    Key arguments:
    letter -- a string to be converted
    """
    title_case = ''
    should_be_upper = True
    for index, letter in enumerate(text):
        if letter.isalpha():
            if should_be_upper:
                title_case += letter.upper()
                should_be_upper = False
            else:
                title_case += letter.lower()
                should_be_upper = False
        else:
            title_case += letter
            should_be_upper = True
    return title_case

# Testing function:
assert getTitleCase('Hello, world!') == 'Hello, World!'
assert getTitleCase('HELLO') == 'Hello'
assert getTitleCase('hello') == 'Hello'
assert getTitleCase('hElLo') == 'Hello'
assert getTitleCase('') == ''
assert getTitleCase('abc123xyz') == 'Abc123Xyz'
assert getTitleCase('cat dog RAT') == 'Cat Dog Rat'
assert getTitleCase('cat,dog,RAT') == 'Cat,Dog,Rat'