letter = '''Dear <|NAME|>,We are pleased to inform you that you have been selected for the position of <|POSITION|>'''
#print(letter.replace("<|NAME|>", "anant kumar").replace("<|POSITION|>", "AI and ML Engineer"))
a =input("Enter your name: ")
b = input("Enter your position: ")
print(letter.replace("<|NAME|>", a).replace("<|POSITION|>", b))
