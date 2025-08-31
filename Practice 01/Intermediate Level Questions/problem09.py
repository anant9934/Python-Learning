#Create a program that prints a multiplication table for numbers 1 to 5.
def tab(n):
    for i in range (1,11):
        print(f"{n} * {i} = {n*i}")

tab(1)
tab(2)
tab(3)
tab(4)
tab(5)