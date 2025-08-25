age = int(input("Enter your age: "))
#if statement no :1
if age%2 == 0:
    print("Your age is even")
else:
    print("Your age is odd")
# --- IGNORE ---

# if statement no :2
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
# --- IGNORE ---
print("Thank you for using the age checker!")