# Exercise #6: Ordinal Suffix

def ordinalSuffix(number: int) -> str:
    str_num = str(number)
    # Special cases 11th, 12th and 13th
    if len(str_num) > 1 and str_num[-2] == '1':
        return str_num + 'th'
    else:
        if  str_num[-1] == '1':
            return str_num + 'st'
        elif  str_num[-1] == '2':
            return str_num + 'nd'
        elif  str_num[-1] == '3':
            return str_num + 'rd'
        else:
            return str_num + 'th'  

# Testing the function
assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'
