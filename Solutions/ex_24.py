# Exercise #24: Every 15 Minutes

def every15Minutes() -> str:
    """ Return all every possible display at an AM/PM clock with 15 minutes intervals.
    
    Key arguments:
    None
    """
    for period in ['am', 'pm']:
        for hour in ['12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
            for minutes in ['00', '15', '30', '45']:
                print(f"{hour}:{minutes} {period}")

# Testing function
every15Minutes()

