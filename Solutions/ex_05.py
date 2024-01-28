# Exercise #5: Fizz Buzz

def fizzBuzz(uoTo: int):
    """Return the results of a Fizz Buzz game.
    
    Key arguments:
    upTo -- last integer number to evaluate in the sequence
    """
    for number in range(1, uoTo+1):
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz', end=' ')
        elif number % 3 == 0:
            print('Fizz', end=' '),
        elif number % 5 == 0:
            print('Buzz', end=' '),
        else:
            print(number, end=' '),

fizzBuzz(35)