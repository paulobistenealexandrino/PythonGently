# Exercise #17: Dice Roll
import random
random.seed(42)

def rollDice(numberOfDice: int) -> int:
    """Return the sum of multiple 6 faces dice rolls.
    
    Key argument:
    numberOfDice -- number of 6 faces dices to roll
    """
    sum_rolls = 0
    for die in range(numberOfDice):
        sum_rolls += random.randint(1, 6)
    return sum_rolls

# Testing function
assert rollDice(0) == 0
assert rollDice(1000) != rollDice(1000)
for i in range(1000):
    assert 1 <= rollDice(1) <= 6
    assert 2 <= rollDice(2) <= 12
    assert 3 <= rollDice(3) <= 18
    assert 100 <= rollDice(100) <= 600