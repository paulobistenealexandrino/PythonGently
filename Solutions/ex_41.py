# Exercise #41: ROT 13 Encryption

def rot13(text: str) -> str:
    """Return the ROT 13 encrypted version of text.
    
    Key arguments:
    text -- string to be encrypted
    """
    text = str(text)
    LETTERS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z')
    encrypted_text = str()

    for i, letter in enumerate(text):
        if not text[i].isalpha():
            encrypted_text += text[i]
            continue

        if text[i].isupper():
            if LETTERS.index(letter.lower()) < 13:
                encrypted_text += LETTERS[LETTERS.index(letter.lower())+13].upper()
            else:
                encrypted_text += LETTERS[LETTERS.index(letter.lower())-13].upper()
            continue

        if text[i].islower():
            if LETTERS.index(letter) < 13:
                encrypted_text += LETTERS[LETTERS.index(letter)+13]
            else:
                encrypted_text += LETTERS[LETTERS.index(letter)-13]
            continue

    return encrypted_text

# Testing function
assert rot13('Hello, world!') == 'Uryyb, jbeyq!'
assert rot13('Uryyb, jbeyq!') == 'Hello, world!'
assert rot13(rot13('Hello, world!')) == 'Hello, world!'
assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'
assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'