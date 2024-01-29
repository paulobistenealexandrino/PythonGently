# Exercise #14: Average

def average(numbers):
    """Calculate the averege.
    
    Key arguments:
    numbers -- a collection of number values
    """
    if numbers == []:
        return None
    else:
        sum = 0
        for i in range(len(numbers)):
            sum += numbers[i]
        return sum/len(numbers)

# Testing function
assert average([1, 2, 3]) == 2
assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
assert average([12, 20, 37]) == 23
assert average([0, 0, 0, 0, 0]) == 0

import random

random.seed(42)

testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]

for i in range(1000):
    random.shuffle(testData)
    assert average(testData) == 2