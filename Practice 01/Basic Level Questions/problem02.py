#What is the difference between `range(5)`, `range(1, 5)`, and `range(1, 10, 2)`?
for i in range (5):
    print(i)
print("range (5) prints numbers from 0 to 4")
print("_______________________________________________________________________")
for i in range (1,5):
    print(i)
print("range (1,5) prints numbers from 1 to 4")
print("_______________________________________________________________________")
for i in range (1,10,2):
    print(i)
print("range (1,10,2) prints numbers from 1 to 9 with a gap of 2")
print("_______________________________________________________________________")