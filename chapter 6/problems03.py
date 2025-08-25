p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

messages = input("Enter the messages: ")

if p1 in messages or p2 in messages or p3 in messages or p4 in messages:
    print("Spam")
else:
    print("Not Spam")