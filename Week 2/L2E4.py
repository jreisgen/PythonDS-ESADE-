'''Exercise 4: Temperature Converter
1. Define a Conversion Function: Write a function celsius_to_fahrenheit(celsius) that converts Celsius to Fahrenheit.
2. Print the Result: Output the converted temperature for 22ºF, 46ºF, 51ºF and 76ºF.'''

def celcius_to_fahrenheit(celcius):
    return celcius*1.8 + 32


celList = [22, 46, 51, 76]
for cel in celList:
    print(celcius_to_fahrenheit(cel))