a = input("enter your username: ")

b = len(a)
if b < 10:
    print("Username is valid.")
else:
    print("Username is invalid. It must be less than 10 characters.")