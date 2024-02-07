# Exercise #39: Collatz Sequence

def collatz(startingNumber):
  """Return a Collatz sequence.

  Key arguments:
  startingNumber -- first number in the sequence
  """
  collatz_sequence = [startingNumber]
  last_number = startingNumber

  if startingNumber == 0:
    return []

  while True:
    if last_number % 2 == 0:
      last_number /= 2
      collatz_sequence.append(last_number)
    elif (last_number % 2 != 0) and (last_number > 1):
      last_number = 3*last_number + 1
      collatz_sequence.append(last_number)
    else:
      break
  return collatz_sequence

# Testing functions
assert collatz(0) == []
assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]
assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
assert len(collatz(256)) == 9
assert len(collatz(257)) == 123

import random
random.seed(42)
for i in range(1000):
    startingNum = random.randint(1, 10000)
    seq = collatz(startingNum)
    assert seq[0] == startingNum # Make sure it includes the starting number.
    assert seq[-1] == 1  # Make sure the last integer is 1.