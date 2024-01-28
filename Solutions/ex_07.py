# Exercise #7: ASCII Table

def printASCIITable() -> str:
    """Return ASCII numbers and its corresponding text characters."""
    for i in range(32, 127):
        print(i, chr(i))

printASCIITable()