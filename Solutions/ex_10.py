# Exercise #10: Find and Replace

def findAndReplace(text: str, oldText: str, newText: str) -> str:
    """Find and replace a text.
    
    Key arguments:
    text -- string with the text replaced;
    oldText -- text to be replaced;
    newText -- replacement text
    """
    i = 0
    replacedText = ''
    while i < len(text):
        if text[i:i+len(newText)] == oldText:
            replacedText += newText
            i += len(newText)
        else:
            replacedText += text[i]
            i += 1
    return replacedText

# Testing function
assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'
assert findAndReplace('fox', 'fox', 'dog') == 'dog'
assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'
assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'
assert findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'