#store two diff things in a 2d dictionaries

import os, time, random

trumps = {}
trumps["Javi"] = {"shredding": 178, "Speed": 100, "Strength": 150, "Baldness": 99}
trumps["Yoda"] = {"shredding": 0, "Speed": 150, "Strength": 200, "Baldness": 99}
trumps["Iron man"] = {"shredding": 0, "Speed": 200, "Strength": 250, "Baldness": 0}
trumps["Scooby doo"] = {"shredding": 50, "Speed": 100, "Strength": 175, "Baldness": 0}

while True:
    print("Top Trumps")
    print()
    print("Characters")
    print()
    for key in trumps:
        print(key)
    user = input("pick your character\n> ")
    comp = random.choice(list(trumps.keys()))
    print("Computer has picked", comp)

    print("choose your stat: shredding, Speed, Strength, and Baldness")

    answer = input("> ")

    print(f"{user}: {trumps[user][answer]}")
    print(f"{comp}: {trumps[comp][answer]}")
    
    if trumps[user][answer] > trumps[comp][answer]:
        print(user, "wins")
    elif trumps[user][answer] < trumps[comp][answer]:
        print(comp, "wins")
    else:
        print("draw")

    time.sleep(2)
    os.system("clear")
    
