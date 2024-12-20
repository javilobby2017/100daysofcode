#day 49 solution

import os, time

f = open("high.score", "r")
scores = f.read().split("\n")
f.close()

highscore = 0
name = None

for rows in scores:
    data = rows.split()
    print(data)
    if not data != []:
        if int(data[1]) > highscore:
            highscore = int(data[1])
            name = data[0]
print("the winner is", name, "with", highscore)