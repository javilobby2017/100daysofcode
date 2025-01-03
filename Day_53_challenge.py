import os, time
inventory = []

try:
    f = open("inventory.txt", "r")
    inventory = eval(f.read())
    f.close()
except:
    pass
#passing subroutines to test inventory text file
def additem():
    time.sleep(1)
    os.system("clear")
    print("INVENTORY")
    print("=========")
    print()
    item = input("item to add > ").capitalize()
    inventory.append(item)
    print("Added")


def viewitem():
    time.sleep(1)
    os.system("clear")
    print("INVENTORY")
    print("=========")
    print()
    seen = []
    for item in inventory:
        if item not in seen:
            print(f"{item} {inventory.count(item)}")
            seen.append(item)

    time.sleep(2)



def removeitem():
    time.sleep(1)
    os.system("clear")
    print("INVENTORY")
    print("=========")
    print()
    item = input("item to remove> ").capitalize()
    if item in inventory:
        inventory.remove(item)
        print("removed")
    else:
        print("you dont have that item")


while True:
    time.sleep(1)
    os.system("clear")
    print("INVENTORY")
    print("=========")
    print()
    menu = input("1: add\n2: view\n3: remove\n")
    if menu == "1":
        additem()
    elif menu == "2":
        viewitem()
    else:
        removeitem()
    
    f = open("inventory.txt", "w")
    f.write(str(inventory))
    f.close()

