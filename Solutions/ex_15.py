# Exercise #15: Median

def median(numbers):
    """Calculate the median
    
    Key arguments:
    numbers -- a collection of number values
    """
    numbers.sort()
    if numbers == []:
        return None
    elif len(numbers) % 2 == 0:
        middle_left = int((len(numbers)/2) - 1)
        middle_right = int(len(numbers)/2)
        return (numbers[middle_left] + numbers[middle_right])/2
    else:
        middle_position = int(len(numbers)/2)
        return numbers[middle_position]
    
# Testing numbers
assert median([]) == None
assert median([1, 2, 3]) == 2
assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5
assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6
import random
random.seed(42)
testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]
for i in range(1000):
    random.shuffle(testData)
    assert median(testData) == 6