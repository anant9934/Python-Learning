# if elif else ladder
age = int(input("Enter your age: "))
if age < 0:
    print("Invalid age")
elif age < 18:
    print("You are a minor")
elif age < 65:
    print("You are an adult")
elif age < 100:
    print("You are a senior citizen")
else:
    print("You are a centenarian")
print("Thank you for using the age checker!")