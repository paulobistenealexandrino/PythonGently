# Exercise #31 - Convert Integer to Strings

"I couldn't solve this problem by myself. I had to look the solution"

def convertIntToStr(integerNum: int) -> str:
    """Convert a integer number in a string.
    
    Key arguments:
    integerNum -- integer number to be converted
    """
    if integerNum == 0:
        return '0'
    
    NUMERALS = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    
    if integerNum < 0:
        is_negative = True
        integerNum = -1*integerNum
    else:
        is_negative = False
    
    stringNum = ''

    while integerNum > 0:
        ones_place_digit = integerNum % 10
        stringNum = NUMERALS[ones_place_digit] + stringNum
        integerNum //= 10

    if is_negative:
        return '-' + stringNum
    else:
        return stringNum

# Testing function
for i in range(-10000, 10000):
    assert convertIntToStr(i) == str(i)