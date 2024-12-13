import random,os,time

print("bingo card generator")

bingo = []

def generate_random_number():
    number = random.randint(1,90)
    return number

def prettyPrint():
    for row in bingo:
        for item in row:
            print(item, end=" | ")
        print()

def createCard():
    global bingo
    numbers = []
    for i in range(8):
        numbers.append(generate_random_number())

    numbers.sort()


    bingo = [[numbers[0], numbers[1], numbers[2]],
            [numbers[3],"BINGO",numbers[4]],
            [numbers[5],numbers[6],numbers[7]]]

createCard()

while True:
    prettyPrint()
    num = int(input("Next Number: ")) 
    found = False
    for row in range(3):
        for item in range(3):
            if bingo[row][item] == num:
                bingo[row][item] = "X"
                found = True
                print(f"Marked {num} as 'X'.")
    exes = 0
    for row in bingo:
        for item in row:
            if item=="X":
                exes+=1
    if exes == 8:
        print("you have won")
        break
    if not found:
        print(f"Number {num} not found on the bingo card.")

    time.sleep(1)
    os.system("clear")


