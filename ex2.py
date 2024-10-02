mixedList = [3, "string", 4.21, "string", 3.12, 4]
ints = [i for i in mixedList if type(i)== int]
print(ints)