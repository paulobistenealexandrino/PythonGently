# Exercise #3: Comma-Formatted Numbers
def commaFormat(number):
    """Return a formated integer or float number where digits are grouped with commas.
    
    Key arguments:
    number -- number to be formatted
    """
    if type(number) not in (int, float):
        return print('number must be of type int or float')

    if type (number) == float:
        is_float = True
        number = list(str(number))
        float_point_position = number.index('.')
        number_list = number[:float_point_position]
        decimal_part_list = number[float_point_position:len(number)]
    else:
        is_float = False
        number_list = list(str(number))
        
    if len(number_list) > 3:
        position = len(number_list)
        if len(number_list) % 3 == 0:
            number_of_commas = (len(number_list) // 3) - 1
        else:
            number_of_commas = len(number_list) // 3
        count_algarisms = 0
        commas_added = 0
        while commas_added < number_of_commas:
            if count_algarisms == 3:
                commas_added += 1
                number_list.insert(position, ',')
                count_algarisms = 0
            position -= 1
            count_algarisms += 1
    formatted_number = ''.join(number_list)

    if is_float:
        return formatted_number + ''.join(decimal_part_list)
    else:
        return formatted_number

# Testing function
assert commaFormat(1) == '1'
assert commaFormat(10) == '10'
assert commaFormat(100) == '100'
assert commaFormat(1000) == '1,000'
assert commaFormat(10000) == '10,000'
assert commaFormat(100000) == '100,000'
assert commaFormat(1000000) == '1,000,000'
assert commaFormat(1234567890) == '1,234,567,890'
assert commaFormat(1000.123456) == '1,000.123456'
