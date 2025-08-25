a = int(input("Enter your marks: "))
if a >= 90 and a <= 100:
    print("You got an O+ grade.")
elif a >= 80 and a < 90:
    print("You got an A grade.")
elif a >= 70 and a < 80:
    print("You got a B grade.")
elif a >= 60 and a < 70:
    print("You got a C grade.")
elif a >= 50 and a < 60:
    print("You got a D grade.")
elif a < 50:
    print("You got an F grade.")
else:
    print("You enterd invalid marks.")