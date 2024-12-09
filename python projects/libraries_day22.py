import random
myNumber = random.randint(1,100)
guess_count = 0
while True:
  guess = int(input("Guess a number between 1 and 100: "))
  if guess < myNumber and guess_count < 50:
    print("too low")
    guess_count += 1
  if guess > myNumber and guess_count < 100:
    print("too high")
    guess_count += 1
  if guess == myNumber:
    print("Thats correct! it took you", guess_count, "tries")
    break