a = int(input("Enter your physics marks: "))
b = int(input("Enter your chemistry marks: "))
c = int(input("Enter your maths marks: "))


total_marks = a + b + c
perecentage = (total_marks / 300) * 100

if perecentage >= 40 and a >= 33 and b >= 33 and c >= 33:
    print("You are passed.")
else:
    print("You are failed.")