import os, time

myAgenda = []

def printList():
    print()
    for item in myAgenda:
        print(item)
    print()

while True:
    menu = input("Add or Remove?:")
    if menu == "Add":
        item = input("What's next on the Agenda?:")
        myAgenda.append(item)
    elif menu == "Remove":
        item = input("what do you want to remove?:")
        if item in myAgenda:
            myAgenda.remove(item)
        else:
            print(f"{item} was not on the list")
    printList()

