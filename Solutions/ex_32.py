# Exercise #32: Convert Strings to Integers

def convertStrToInt(strNum: str) -> int:
    """Convert a numeral string to a integer
    
    Key arguments:
    strNum -- a numeral in a string format to be converted
    """
    NUMERALS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    intNum = 0
    
    if strNum[0] == '-':
        is_negative = True
        strNum = strNum[1:len(strNum)]
    else:
        is_negative = False

    for i, key in enumerate(strNum):
        intNum += NUMERALS[key]*10**(len(strNum)-i-1)

    if is_negative:
        return -1*intNum
    else:
        return intNum
    
# Testing function
for i in range(-10000, 10000):
    assert convertStrToInt(str(i)) == i

