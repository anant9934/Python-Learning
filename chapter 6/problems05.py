a = ["aryan", "anant", "mandeep", "prince", "sahil"]
b = input("Enter your username: ")
if b in a:
    print("Username is valid.")
else:
    print("Username is invalid. It must be one of the following: "+" ".join(a))      #This line concatenates the list of valid usernames into a string for the error message.
    print("Please try again.")