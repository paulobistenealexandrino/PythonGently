# Exercise #13: Sum & Product

def calculateSum(numbers):
    """Return the sum of all the numbers on the list
    
    Key arguments:
    numbers -- a collection of number values
    """
    if numbers == []:
        return 0
    else:
        sum = 0
        for i in range(len(numbers)):
            sum += numbers[i]
    return sum

def calculateProduct(numbers):
    """Return the product of all the numbers on the list
    
    Key arguments:
    numbers -- a collection of number values
    """
    if numbers == []:
        return 1
    else:
        product = 1
        for i in range(len(numbers)):
            product *= numbers[i]
    return product

# Testing functions
assert calculateSum([]) == 0
assert calculateSum([2, 4, 6, 8, 10]) == 30
assert calculateProduct([]) == 1
assert calculateProduct([2, 4, 6, 8, 10]) == 3840
