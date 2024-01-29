# Exercise #12: Smallest & Biggest

def getSmallest(numbers):
    """Return the smallest number on the list
    
    Key arguments:
    numbers -- a collection of number values
    """
    if type(numbers) == int:
        return numbers
    elif numbers == []:
        return None
    else:
        smallest = numbers[0]
        for i in range(len(numbers)):
            if numbers[i] <= smallest:
                smallest = numbers[i]
        return smallest
    
def getBiggest(numbers):
    """Return the biggest number on the list
    
    Key arguments:
    numbers -- a collection of number values
    """
    if type(numbers) == int:
        return numbers
    elif numbers == []:
        return None
    else:
        biggest = numbers[0]
        for i in range(len(numbers)):
            if numbers[i] >= biggest:
                biggest = numbers[i]
        return biggest
        
# Testing function
assert getSmallest([1, 2, 3]) == 1
assert getSmallest([3, 2, 1]) == 1
assert getSmallest([28, 25, 42, 2, 28]) == 2
assert getSmallest([1]) == 1
assert getSmallest([]) == None
assert getBiggest([1, 2, 3]) == 3
assert getBiggest([3, 2, 1]) == 3
assert getBiggest([28, 25, 42, 2, 28]) == 42
assert getBiggest([1]) == 1
assert getBiggest([]) == None