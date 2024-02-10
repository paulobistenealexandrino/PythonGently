# Exercise #38: Random Shuffle
import random

def shuffle(values: list) -> list:
    """Shuffle the values is a list.
    
    Key arguments:
    values -- a list containing values
    """
    shuffled_values = list()
    number_of_elements = len(values)
    for i in range(0, number_of_elements):
        random_index = random.randint(0, len(values) - 1)
        popped_item = values.pop(random_index)
        values.append(popped_item)

# Testing function
# Perform this test ten times:
for i in range(10):
    testData1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    shuffle(testData1)
    # Make sure the number of values hasn't changed:
    assert len(testData1) == 10
    # Make sure the order has changed:
    assert testData1 != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Make sure that when re-sorted, all the original values are there:
    assert sorted(testData1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Make sure an empty list shuffled remains empty:
testData2 = []
shuffle(testData2)
assert testData2 == []
