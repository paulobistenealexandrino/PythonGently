# Exercise #8: Read Write File

def writeToFile(file: str, text: str):
    """Create the file and write the text to it.
    
    Key arguments:
    file -- file name;
    text -- text to write on the file
    """
    with open(file, mode='w') as temp_file:
        temp_file.write(text)

def appendToFile(file: str, text: str):
    """Append the text to the file.
    
    Key arguments:
    file -- file name;
    text -- text to write on the file
    """
    with open(file, mode='a') as temp_file:
        temp_file.write(text)

def readFromFile(file: str):
    """Read the file.
    
    Key arguments:
    file -- file name
    """
    with open(file, mode='r') as temp_file:
        return temp_file.read()

# Testing functions
writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'
