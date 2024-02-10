# Exercise #34: Uppercase Letters

def getUppercase(text: str) -> str:
    """Return the text in uppercase letters.
    
    Key arguments:
    text -- text to be converted in uppercase
    """
    text = str(text)
    LETTERS = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E',
               'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J',
               'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O',
               'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T',
               'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y',
               'z': 'Z'}
    
    uppercase_text = ''
    for character in text:
        if character in LETTERS.keys():
            uppercase_text += LETTERS[character]
        else:
            uppercase_text += character
    return uppercase_text

# Testing function
assert getUppercase('Hello') == 'HELLO'
assert getUppercase('hello') == 'HELLO'
assert getUppercase('HELLO') == 'HELLO'
assert getUppercase('Hello, world!') == 'HELLO, WORLD!'
assert getUppercase('goodbye 123!') == 'GOODBYE 123!'
assert getUppercase('12345') == '12345'
assert getUppercase('') == ''

