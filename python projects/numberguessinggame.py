correct_number = 50
guess_count = 0
while True:
  guess = int(input("Guess a number between 1 and 100: "))
  if guess < 50:
    print("too low")
    guess_count += 1
  if guess > 100:
    print("too high")
    guess_count += 1
  if guess == 50:
    print("Thats correct! it took you", guess_count, "tries")
    break