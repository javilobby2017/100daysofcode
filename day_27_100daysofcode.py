import random, os, time

def rollDice(side):
    result = random.randint(1,side)
    return result
def health():
    healthStat = ((rollDice(6)*rollDice(12))/2)+10
    return healthStat
def strength():
    strengthStat = ((rollDice(6)*rollDice(12))/2)+12
    return strengthStat


print("Battle Time")
print()
c1Name = input("Name your legend: ")
c1Type = input("Character type (Human, Elf, Hunter, Wizard, Orc)")
print()
print(c1Name)
c1Health = health()
c1Strength = strength()
print("health:", c1Health)
print("strength:", c1Strength)
print()
print("Who are they battling?")

print()
c2Name = input("Name your legend: ")
c2Type = input("Character type (Human, Elf, Hunter,other: )")
print()
print(c2Name)
c2Health = health()
c2Strength = strength()
print("health:", c2Health)
print("strength:", c2Strength)
print()

round = 1
winner = None

while True:
    time.sleep(1)
    os.system("clear")
    print("Battle Time")
    print()
    print("The Batltle Begins!")

    c1Dice = rollDice(6)
    c2Dice = rollDice(6)

    difference = abs(c1Strength - c2Strength) + 1

    if c1Dice > c2Dice:
        c2Health -= difference
        if round == 1:
            print(c1Name, "wins the first blow")
        else:
            print(c1Name,"wins round", round)
    
    elif c2Dice > c1Dice:
        c1Health -= difference
        if round == 1:
            print(c2Name, "wins the first blow")
        else:
            print(c2Name,"wins round", round)
    else:
        print("There is a draw",round)
    
    print()
    print(c1Name)
    print("health:", c1Health)
    print()
    print(c2Name)
    print("health:", c2Health)
    print()

    if c1Health <= 0:
        print(c1Name,"died")
        winner = c2Name
        break
    elif c2Health <= 0:
        print(c2Name, "died")
        winner = c1Name
        break
    else:
        print("they are both standing for the next round")
        round += 1


time.sleep(1)
os.system("clear")
print("Battle Time")
print()
print(winner, "has won in", round,"rounds")



