# Exercise #29: Pyramid Drawing

def drawPyramid(height: int) -> str:
    """Draw a pyramid.
    
    Key arguments:
    height -- the height of the pyramid
    """
    blank_spaces = height - 1
    for h in range(height):
        print(' '*blank_spaces + '#'*(2*h + 1) + ' '*blank_spaces)
        blank_spaces -= 1

drawPyramid(30)