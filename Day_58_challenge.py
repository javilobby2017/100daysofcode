import random, os, time
totalAttempts = 0

def game():
    attempts = 0
    while True:
        number = random.randint(1,100)
        guess = int(input("pick a number between 1 and 100"))
        if guess > number:
            print("too high")
            attempts+=1
        elif guess < number:
            print("too low")
            attempts+=1
        else:
            print("just right")
            print(f"{attempts} attempts this round")
        