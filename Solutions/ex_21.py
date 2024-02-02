# Exercise #21: Validade Date

def isLeapYear(year: int) -> bool:
    """Return True if a year is leap year.
    
    Key arguments:
    year -- year to be checked as leap
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def isValidDate(year: int, month: int, day: int) -> bool:
    if (day < 1) or (month < 1) or (year < 1):
        return False
    elif month not in range(1, 13):
        return False
    elif (month in [1, 3, 5, 7, 8, 10, 12]) and (day > 31):
        return False
    elif (month in [4, 6, 9, 11]) and (day > 30):
        return False
    elif (month == 2) and (day > 29):
        return False
    elif (month == 2) and (day == 29) and (not isLeapYear(year)):
        return False
    else:
        return True

# Testing function
assert isValidDate(1999, 12, 31) == True
assert isValidDate(2000, 2, 29) == True
assert isValidDate(2001, 2, 29) == False
assert isValidDate(2029, 13, 1) == False
assert isValidDate(1000000, 1, 1) == True
assert isValidDate(2015, 4, 31) == False
assert isValidDate(1970, 5, 99) == False
assert isValidDate(1981, 0, 3) == False
assert isValidDate(1666, 4, 0) == False
import datetime
d = datetime.date(1970, 1, 1)
oneDay = datetime.timedelta(days=1)
for i in range(1000000):
    assert isValidDate(d.year, d.month, d.day) == True
    d += oneDay