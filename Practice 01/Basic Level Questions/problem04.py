#Explain the difference between `break` and `continue` statements with examples.
# using while loop
i = 1
while i <= 100:
    print (i)
    i += 1
    if i == 34:
        break

print("break function will exist the loop when i = 34 ")
print("_______________________________________________________________________")
i = 1
while i <= 100:
    if i == 34:
        i += 1
        continue
  
    print (i)
    i += 1

print("continue function will skip the value and continue the loop when i = 34 ")
print("_______________________________________________________________________")

#using for loop:
for i in range (0,100):
    print(i)
    if i == 34:
        break
print("break function will exist the loop when i = 34 ")
print("_______________________________________________________________________")

for i in range (0,100):
    if i == 34:
        continue
    print(i)
print("continue function will skip the value and continue the loop when i = 34 ")
print("_______________________________________________________________________")