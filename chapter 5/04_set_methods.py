a = {1, 2, 3, 4, 5} # This is a set containing unique elements
d = {1, 2, 3, 4, 5, "anant"}
print(type(d)) # This will print <class 'set'>, sets can contain different data types
print(len(d)) # This will print the number of unique elements in the set
# print(d[0]) # This will raise an error, sets are unordered and do not support indexing
g = a.add(6) # This will add 6 to the set a
print(a) # This will print {1, 2, 3, 4, 5, 6}
h = a.remove(1) # This will remove 1 from the set a
print(a) # This will print {2, 3, 4, 5, 6}
i = a.discard(2) # This will remove 2 from the set a, if it exists
print(a) # This will print {3, 4, 5, 6}
j = a.pop() # This will remove and return an arbitrary element from the set a
print(j) # This will print the element that was removed
print(a) # This will print the set after the pop operation
k = a.clear() # This will remove all elements from the set a
print(k) # This will print an empty set set()   