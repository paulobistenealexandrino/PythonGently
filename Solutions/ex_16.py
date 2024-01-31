# Exercise #16: Mode

def mode(numbers):
    """Return the mode
    
    Key arguments:
    numbers -- a collection of numeric values
    """
    if numbers == []:
        return None
    else:
        numbers_list = list(set(numbers))
        numbers_dictionary = {n: None for n in numbers_list}
        for key in numbers_dictionary:
            count = 0
            for item in numbers:
                if key == item:
                    count += 1
            numbers_dictionary[key] = count
        biggest = 1
        for key in numbers_dictionary:
            if numbers_dictionary[key] > biggest:
                biggest = numbers_dictionary[key]
                mode = key
    return mode

# Testing function
assert mode([]) == None
assert mode([1, 2, 3, 4, 4]) == 4
assert mode([1, 1, 2, 3, 4]) == 1
import random
random.seed(42)
testData = [1, 2, 3, 4, 4]
for i in range(1000):
    random.shuffle(testData)
    assert mode(testData) == 4