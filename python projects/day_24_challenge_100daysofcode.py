import random
ask = int(input("how many sides?: "))
playAgain = "yes"

def infinityDice(ask):
    value= random.randint(1,ask)
    print("You rolled a " + str(value))
while playAgain == "yes":
    infinityDice(ask)
    playAgain = input("Roll again?")