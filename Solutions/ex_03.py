# Exercise #3: Odd & Even

def isOdd(number: int) -> bool:
    """Return True if a given integer number is odd, and False otherwise.
    
    Key arguments:
    number -- an integer number to be evaluated 
    """
    return type(number) == int and number % 2 != 0

def isEven(number: int) -> bool:
    """Return True if a given integer number is even, and False otherwise.
    
    Key arguments:
    number -- an integer number to be evaluated 
    """
    return type(number) == int and number % 2 == 0

# Testing functions
assert isOdd(42) == False
assert isOdd(9999) == True
assert isOdd(-10) == False
assert isOdd(-11) == True
assert isOdd(3.1415) == False
assert isEven(42) == True
assert isEven(9999) == False
assert isEven(-10) == True
assert isEven(-11) == False
assert isEven(3.1415) == False
