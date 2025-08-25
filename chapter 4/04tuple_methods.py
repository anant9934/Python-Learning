e = (1, 856, 56.59, True, "sachin", "aakash", "rohiyt", 856)
a = (1, 2, 3, 4, 5)  # Defining a tuple with integers
print(e)  # Printing the tuple with mixed data types

no = e.count(856)  # Counting occurrences of 856 in the tuple
print(no)  # Printing the count of 1 in the tuple

print(e.index(856))  # Finding the index of the first occurrence of 856 in the tuple

print(a[1:3])  # Slicing the tuple to get elements from index 1 to 2 (exclusive of 3)
print(a+e)  # Concatenating two tuples
print(a*2)  # Repeating the tuple 'a' two times
print(len(a))  # Getting the length of the tuple 'a'

b = list(a)  # Converting tuple 'a' to a list
print(b)  # Printing the list converted from tuple 'a'
print(type(b))  # Printing the type of 'b' to confirm it is a list

c = tuple(b)  # Converting the list 'b' back to a tuple
print(c)  # Printing the tuple converted from list 'b'
print(type(c))  # Printing the type of 'c' to confirm it is a tuple