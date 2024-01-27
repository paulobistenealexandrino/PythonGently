# Exercise #2: Temperature Conversion

def convertToFahrenheit(degreesCelsius: float) -> float:
    """Convert the temperature from degrees Celsius to degrees Fahrenheit.
    
    Key arguments:
    degreesCelsius -- the temperature in degrees Celsius 
    """
    degreesFahrenheit = degreesCelsius*(9/5) + 32
    print(degreesFahrenheit)
    return degreesFahrenheit

def  convertToCelsius(degreesFahrenheit: float) -> float:
    """Convert the temperature from degrees Fahrenheit to degrees Celsius.
    
    Key arguments:
    degreesFahrenheit -- the temperature in degrees Fahrenheit
    """
    degreesCelsius = (degreesFahrenheit - 32)*(5/9)
    print(degreesCelsius)
    return degreesCelsius

# Testing the functions
assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15

# Rounding errors cause a slight discrepancy:
assert convertToCelsius(convertToFahrenheit(42)) == 42.00000000000001