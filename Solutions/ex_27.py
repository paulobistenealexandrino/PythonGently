# Exercise #27: Rectangle Drawing

def drawRectangle(width: int, height: int) -> str:
    """Draw a rectangle using #.
    
    Key arguments:
    width -- the rectangles width measured in numbers of # symbols;
    height -- the rectangles height measured in numbers of #
    """
    line = ''
    for w in range(width):
        line += '#'
    for h in range(height):
        print(line)

# Testing the function
drawRectangle(10, 4)