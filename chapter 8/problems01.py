# write a programe using function to find greatest of three numbers 

a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))


def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c


print("greatest number written amoungust you is,", greatest(a,b,c))

