def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))
    
    average = (a + b + c) / 3
    return average  # Use return instead of print

result = avg()  # Store the returned value
print("The average of the three numbers is:", result)