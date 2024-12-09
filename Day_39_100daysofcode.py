import random , os, time

listOfWords = ["british", "suave", "bald", "integerity", "evil", "genius"]
letterPicked = []
lives = 6
myWord = random.choice(listOfWords)

while True:
    time.sleep(1)
    os.system("clear")
    letter = input("Choose a letter: ").lower()
    
    if letter in letterPicked:
        print("You've tried that before")
        continue
    
    letterPicked.append(letter)
    
    if letter in myWord:
        print("you found a letter")
    else:
        print("Nope, not in there")
        lives -= 1
    allLetters = True
    print()
    for i in myWord:
        if i in letterPicked:
            print(i, end="")
        else:
            print("_", end="")
            allLetters = False
    print()

    if allLetters:
        print(f"Congrats! you guessed the word!")

    if lives == 0:
        print(f"you ran out of lives! the answer was '{myWord}'.")
        break
   
    print(f"Only{lives}left!")
            
