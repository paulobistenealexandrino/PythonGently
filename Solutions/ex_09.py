# Exercise #9: Chess Square Color

def getChessSquareColor(column: int, row: int) -> str:
    """Guess the chess square color based on column and row number.
    
    Key arguments:
    column -- chess square column index number;
    row -- chess square column index number
    """
    if (column < 0 or column > 7) or (row < 0 or row > 7):
        return ''
    elif column % 2 == row % 2:
        return 'white'
    else:
        return 'black'

# Testing function   
assert getChessSquareColor(0, 0) == 'white'
assert getChessSquareColor(1, 0) == 'black'
assert getChessSquareColor(0, 1) == 'black'
assert getChessSquareColor(7, 7) == 'white'
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''