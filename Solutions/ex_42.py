# Exercise #42: Bubble Sort

def bubbleSort(numbers: list) -> list:
    """Sort number in the list.
    
    Key arguments:
    numbers -- list of numbers
    """
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] > numbers[j]:
                popped_item = numbers.pop(j)
                numbers.insert(i, popped_item)
    return numbers

# Testing function
assert bubbleSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]
assert bubbleSort([2, 2, 2, 2]) == [2, 2, 2, 2]