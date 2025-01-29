my_tuple = (1, 2, 3, 4, 5)

print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

print("Elements from index 1 to 3:", my_tuple[1:4])

a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c, d, e)

nested_tuple = (1, 2, (3, 4), 5)
print("Nested tuple:", nested_tuple)
print("Accessing nested element:", nested_tuple[2][1])

