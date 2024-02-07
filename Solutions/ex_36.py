# Exercise #36: Reverse String

def reverseString(text: str) -> str:
  """Return the letters of text in the reverse order.

  Key arguments:
  text -- string to be reversed
  """
  if type(text) != str:
    return 'text must be of type str.'
  reversed_text = ""
  for index, letter in enumerate(text):
    reversed_text = letter + reversed_text
  return reversed_text

# Testing functions
assert reverseString('Hello') == 'olleH'
assert reverseString('') == ''
assert reverseString('aaazzz') == 'zzzaaa'
assert reverseString('xxxx') == 'xxxx'