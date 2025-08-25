# a = int(input("Enter a number: "))
# b = 1
# if a/a != 1  and a < 1 and a/b != a:
#     print(f"{a} is not a prime number")
# else:
#     print(f"{a} is a prime number")
# # This code checks if a number is prime by checking divisibility.
    

n = int(input("Enter a number: "))

for i in range(2, n):
    if n % i == 0:
        print(f"{n} is not a prime number")
        break
else:
    print(f"{n} is a prime number")
# This code checks if a number is prime by checking divisibility.