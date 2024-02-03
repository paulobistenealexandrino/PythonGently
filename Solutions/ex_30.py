def drawBox(size: int) -> str:
    """Draw a box.
    
    Key arguments:
    size -- box size
    """
    print((size + 1)*' ' + '+' + 2*size*'-' + '+')
    blank_space = size
    for i in range(size):
        print(blank_space*' ' + '/' + 2*size*' ' + '/' + i*' ' + '|')
        blank_space -= 1
    print('+' + 2*size*'-' + '+' + size*' ' + '+')
    blank_space = size - 1
    for i in range(size):
        print('|' + 2*size*' ' + '|' + blank_space*' ' + '/')
        blank_space -= 1
    print('+' + 2*size*'-' + '+' + size*' ')

# Testing function
drawBox(2)