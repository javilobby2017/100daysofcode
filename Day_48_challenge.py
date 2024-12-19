import os, time

while True:
    print("scoreboard")
    print()
    name = input("initials > ").upper()
    score = input("score > ")
    print()

    f = open("high.score", "a+")
    f.write(f"{name} {score}\n")
    f.close()

    print("added")
    time.sleep(1)
    os.system("clear")
