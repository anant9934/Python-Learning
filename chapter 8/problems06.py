#write a python functions which converts inch to centimeter
def con(n):
    if 0 <= n <= n:
        return n*(2.54)

n = float(input("enter value in inch whic you want to convert into cm : "))
print(f"{n}inch in cm is around {round(con(n))}cm, exact value is {con(n)}cm")
