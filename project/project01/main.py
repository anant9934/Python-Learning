'''
1 for snake 
-1 for water
0 for gun
'''
import random
computer = random.choice([1,0,-1])
user = str(input("enter your choice out of \"w\",\"g\",\"s\" : "))

youdict = {"w" : -1, "g" : 0, "s" : 1}
revdict = {-1 : "water", 0 : "gun", 1 : "snake"}

user01 = youdict[user] 
user02 = revdict[user01]
computer01 = revdict[computer]

print(f"you chose {user02},and computer chose {computer01}")

if computer == user01:
    print("Draw")


else:
    if computer == -1 and user01 == 0:
        print("you lose")
    elif computer == -1 and user01 == 1:
        print("you win")
    elif computer == 1 and user01 == 0:
        print("you win")
    elif computer == 1 and user01 == -1:
        print("you lose")
    elif computer == 0 and user01 == 1:
        print("you lose")
    elif computer == 0 and user01 == -1:
        print("you win")
    else:
        print("something went wrong")


print("Thanks for playing")
