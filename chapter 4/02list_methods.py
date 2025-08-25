friends = ["anant", 77, 56.59, True, "sachin", "aakash", "rohit"]
print(friends) # Printing the entire list

friends.append("mohan")  # Adding an element to the end of the list
print(friends)  # Printing the modified list

number = [122, 235, 947, 957, 567, 867, 564, 235, 485]
print(number)  # Printing the original list
number.sort()  # Sorting the list in ascending order
print(number)  # Printing the sorted list

friends.insert(2, "mandeep")  # Inserting an element at index 2
print(friends)  # Printing the list after insertion

friends.remove("sachin")  # Removing the element "sachin" from the list
print(friends)  # Printing the list after removal

friends.pop(3)  # Removing the element at index 3
print(friends)  # Printing the list after popping the element