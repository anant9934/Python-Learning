s = {}
a = input("Anant enter your favourite language:   ")
m = input("Mandeep enter your favourite language:   ")
p = input("Prince enter your favourite language:   ")
r = input("Rohan enter your favourite language:   ")
s.update({"anant" : a})
s.update({"mandeep" : m})
s.update({"prince" : p})
s.update({"rohan" : r})
#s.update(anant=a, mandeep=m, prince=p, rohan=r)
print(s)


