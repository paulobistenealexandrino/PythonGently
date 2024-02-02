# Exercise #28: Border Drawing

def drawBorder(width: int, height: int) -> str:
    """Draw a rectangle perimeter.
    
    Key arguments:
    width -- the rectangle's width
    height -- the rectangle's height
    """
    if (width < 3) or (height < 3):
        return print("Width and height must be bigger than 3.")
    for h in range(height):
        if (h == 0) or (h == (height-1)):
            print('+' + '-'*(width-2) + '+')
        else:
            print('|' + ' '*(width-2) + '|')

# Testing function
drawBorder(16, 8)