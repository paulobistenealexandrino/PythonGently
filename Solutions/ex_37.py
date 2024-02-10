# Exercise #37: Change Maker

def makeChange(amount: int) -> dict:
    """Calculate the number of pennies, nickels, dimes and quartes
       for a given amount of change.
       
       Key arguments:
       amount -- amount of change
    """
    COINS = ['quarters', 'dimes', 'nickels', 'pennies']
    
    quarters = amount // 25
    remainder_amount = amount % 25
    
    dimes = remainder_amount // 10
    remainder_amount = remainder_amount % 10

    nickels = remainder_amount // 5
    remainder_amount = remainder_amount % 5

    pennies = remainder_amount

    coins_number = [quarters, dimes, nickels, pennies]

    change = dict()
    for index, denomination in enumerate(COINS):
        if coins_number[index] > 0:
            change[denomination] = coins_number[index]
    return change

# Testing function
assert makeChange(30) == {'quarters': 1, 'nickels': 1}
assert makeChange(10) == {'dimes': 1}
assert makeChange(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}
assert makeChange(100) == {'quarters': 4}
assert makeChange(125) == {'quarters': 5}
