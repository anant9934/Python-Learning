# write a recursive function to find sum of n natural number

def sum(n):
    if 1 <= n <= n:
        return n*(n-1)/2
    else:
        return "not define,because you have to enter any natural number"

n = int(input("enter the natural number you till you want a sum : "))
print("sum of natural number till",n,"is",sum(n))