# Exercise #23: 99 Bottles of Bear

def nineNineBottles() -> str:
    """Return the lyrics of 99 Bottles of Bear.
    """
    import time
    for i in range(99, 0, -1):
        if i > 1:
            print(f"{i} bottles of beer on the wall,\n{i} bottles of beer,\nTake one down,\nPass it around,\n{i - 1} bottles of beer on the wall,\n")
            time.sleep(0.5)           
        else:
            print(f"{i} bottles of beer on the wall,\n{i} bottles of beer,\nTake one down,\nPass it around,\nNo more bottles of beer on the wall.\n")

nineNineBottles()