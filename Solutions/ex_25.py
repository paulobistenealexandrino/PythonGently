# Exercise #25: Multiplication Table

def multiplicationTable() -> str:
    """Print a multiplication table.
    
    Key arguments:
    None
    """
    print('  |  1  2  3  4  5  6  7  8  9 10')
    print('--+-------------------------------')
    for i in range(1, 11):
        line = f"{str(i).rjust(2)}|"
        for j in range(1, 11):
          line += f" {str(i*j).rjust(2)}"  
        print(line)

# Testing function
multiplicationTable()