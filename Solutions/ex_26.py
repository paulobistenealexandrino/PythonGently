# Exercise #26: Handshakes

def printHandshakes(names: list) -> int:
    """Print all possible handshake combinations and return the number of combinations.
    
    Key arguments:
    names -- list of people to combine
    """
    if len(names) <= 1:
        print("There are no handshakes.")
        return 0
    else:
        count = 0
        for i in range(len(names)):
            for j  in range(i+1, len(names)):
                print(f"{names[i]} shakes hands with {names[j]}")
                count += 1
        return count
    
# Testing Function
printHandshakes(['Alice', 'Bob', 'Carol', 'David'])
assert printHandshakes(['Alice', 'Bob']) == 1
assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3
assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6