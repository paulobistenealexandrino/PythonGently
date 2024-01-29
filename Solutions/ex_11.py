# Exercise #11: Hours, Minutes, Seconds

def getHoursMinutesSeconds(totalSeconds: int) -> str:
    """Convert seconds to a hour-ms format.
    
    Key parameters:
    totalSeconds -- number of seconds to convert
    """
    hours = int(totalSeconds / 3600)
    decimalPart_h = (totalSeconds / 3600) - hours
    h = (hours != 0)*f"{hours}h"
    
    minutes = int(decimalPart_h*60)
    decimalPart_m = decimalPart_h*60 - int(decimalPart_h*60)
    m = (minutes != 0)*f"{minutes}m"   
    
    seconds = round(decimalPart_m*60)
    s = (seconds != 0)*f"{seconds}s"

    hms = []
    for component in [h, m, s]:
        if component != '':
            hms.append(component)

    if totalSeconds == 0:
        return '0s'
    else:
        return ' '.join(hms)

# Testing function
assert getHoursMinutesSeconds(30) == '30s'
assert getHoursMinutesSeconds(60) == '1m'
assert getHoursMinutesSeconds(90) == '1m 30s'
assert getHoursMinutesSeconds(3600) == '1h'
assert getHoursMinutesSeconds(3601) == '1h 1s'
assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
assert getHoursMinutesSeconds(90042) == '25h 42s'
assert getHoursMinutesSeconds(0) == '0s'
