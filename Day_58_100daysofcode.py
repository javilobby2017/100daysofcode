import random 
colors = ["red", "orange", "yellow","green", "teal","blue","purple","violet"]
while True:
    menu = input("1: Color or 2: exit?")
    if menu=="1":
        print(random.choice(colors))
    else:
        break