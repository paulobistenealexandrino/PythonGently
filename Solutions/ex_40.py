# Exercise #40: Merging Two Sorted Lists

def mergeTwoLists(list1: list, list2: list) -> list:
    """Return a single sorted list off all numbers from two lists.
    
    Key arguments:
    list1 -- first list
    list2 -- second list
    """
    merged_list = list1 + list2
    is_sorted = False
    while not is_sorted:
        for i in range(0, len(merged_list)-1):
            if merged_list[i] > merged_list[i+1]:
                popped_item = merged_list.pop(i+1)
                merged_list.insert(i, popped_item)

        for i in range(0, len(merged_list)-1):
            if merged_list[i] <= merged_list[i+1]:
                is_sorted = True
            else:
                is_sorted = False
            break
    return merged_list

# Testing function
assert mergeTwoLists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]
assert mergeTwoLists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
assert mergeTwoLists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]
assert mergeTwoLists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]
assert mergeTwoLists([1, 2, 3], []) == [1, 2, 3]
assert mergeTwoLists([], [1, 2, 3]) == [1, 2, 3]


