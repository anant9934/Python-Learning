#5! = 1*2*3*4*5 = 120
'''n = int(input("Enter a number: "))
mul = 1
i = 0
while (i < n):
    i += 1
    mul *= i
print(mul)'''

n = int(input("Enter a number: "))
product = 1
for i in range(1, n + 1):
    product *= i
print(product)