# Exercice #4: Area & Volume

def area(lenght: float, width: float) -> float:
    """Return the area of a rectangle.
    
    Key arguments:
    lenght -- the lenght of the rectangle;
    width -- the width of the rectangle 
    """
    return lenght*width

def perimeter(lenght: float, width: float) -> float:
    """Return the perimeter of a rectangle.
    
    Key arguments:
    lenght -- the lenght of the rectangle;
    width -- the width of the rectangle
    """
    return 2*lenght + 2*width

def volume(lenght: float, width: float, height: float) -> float:
    """Return the volume of a box.
    
    Key arguments:
    lenght -- the lenght of the box;
    width -- the width of the box;
    height -- the height of the box
    """
    return lenght*width*height

def surfaceArea(lenght: float, width: float, height: float) -> float:
    """Return the surface area of a box.
    
    Key arguments:
    lenght -- the lenght of the box;
    width -- the width of the box;
    height -- the height of the box
    """
    return lenght*width*2 + lenght*height*2 + width*height*2

# Testing functions
assert area(10, 10) == 100
assert area(0, 9999) == 0
assert area(5, 8) == 40
assert perimeter(10, 10) == 40
assert perimeter(0, 9999) == 19998
assert perimeter(5, 8) == 26
assert volume(10, 10, 10) == 1000
assert volume(9999, 0, 9999) == 0
assert volume(5, 8, 10) == 400
assert surfaceArea(10, 10, 10) == 600
assert surfaceArea(9999, 0, 9999) == 199960002
assert surfaceArea(5, 8, 10) == 340