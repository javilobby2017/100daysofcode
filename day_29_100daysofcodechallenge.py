#writing subroutine

def newPrint(color, word):
    if(color =="red"):
        print("\033[31m", word, sep="", end="")
    elif(color =="green"):
        print("\033[32m", word, sep="", end="")
    elif(color =="blue"):
        print("\033[34m", word, sep="", end="")
    else:
        print("\033[0m", word, sep="", end="")
print("Super Subroutine")
print("with my ", end="")
newPrint("red", "new program ")
newPrint("reset ", "I can just call red('and')")