# 2D dynamic lists 

listofShame = []

def prettyPrint():
    print()
    for row in listofShame: #make sure not to add () for subroutine
        #adding for loop for item
        for item in row:
            print(f"{item:^10}", end=" | ")
        print()
    print()

while True :
    #adding menu
    menu = input("add or remove?: ")
    if(menu.strip().lower()[0]=="a"):
        name = input("what is your name? ")
        age = input("what is your age? ")
        pref = input("what is your computer platform")
        row = [name, age, pref]
        listofShame.append(row)
        exit = input("Exit? y/n")
    else:
        name = input("what is the name of the record to delete?")
        #adding for loop here 
    for row in listofShame:
        if name in row:
            listofShame.remove(row)
    prettyPrint()