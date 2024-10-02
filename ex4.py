def celcius_to_fahrenheit(celcius):
    return celcius*1.8 + 32


celList = [22, 46, 51, 76]
for cel in celList:
    print(celcius_to_fahrenheit(cel))