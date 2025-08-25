friends = ["anant", 77, 56.59, True, "sachin", "sachin", "sachin"]
print(friends[0])  # Accessing the first element
print(friends[1])  # Accessing the second element
print(friends[2])  # Accessing the third element
print(friends) # Printing the entire list

friends[0] = "rohan"  # Changing the first element,unlike strings, lists are mutable
print(friends)  # Printing the modified list
print(friends[1:4])  # Slicing the list from index 1 to 3 (4 is not included)