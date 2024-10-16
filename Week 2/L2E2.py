'''Exercise 2: Basic Data Filtering
1. Create a List of Mixed Data Types: Create a list that contains a mix of integers, strings, and floats.
2. Filter the List: Use list comprehension to create a new list that contains only the integers from the original list.
3. Print the New List: Output the filtered list of integers.'''

mixedList = [3, "string", 4.21, "string", 3.12, 4]
ints = [i for i in mixedList if type(i)== int]
print(ints)