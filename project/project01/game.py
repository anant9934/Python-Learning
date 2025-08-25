'''
rock = -1
paper = 0
scissor = 1

'''

import random
computer = random.choice([-1,0,1])
user = input("Enter your choice from 'ROCK' 'PAPER' 'SCISSOR' : ")
userdict = {
    "ROCK":-1,
    "PAPER":0,
    "SCISSOR":1
}

computerdict = {
    -1:"ROCK",
    0:"PAPER",
    1:"SCISSOR"
}
comp = computerdict[computer]
user1 = userdict[user]

print(f"your chose {user},and computer chosen {comp}")

if computer == user1:
    print("DRAW")
else:
    if computer == 1 and user1 == 0:
        print("You lose")
    elif computer == 1 and user1 == -1:
        print("You win")
    elif computer == 0 and user == 1:
        print("you win")
    elif computer == 0 and user == -1:
        print("you lose")
    elif computer == -1 and use == 0:
        print("you win")
    elif computer == -1 and user == 1:
        print("you lose")
    else:
        print("something went wrong")