import os, time

toDoList = []

def printList():
    print()
    for items in toDoList:
        print(items)
    print()

while True:
    menu = input("toDoList Manger\nDo you want to view, add, edit,remove or delete the todo list?\n")
    if menu=="view":
        printList()
    elif menu=="add":
        item = input("what would you like to add?\n")
        toDoList.append(item)
    elif menu=="remove":
        item = input("what do you want to remove?\n")
        check = input("are you sure you want to remove this?\n.")
        if check[0]=="y":
            if item in toDoList:
                toDoList.remove(item)
    elif menu =="edit":
        item = input("what do you want to edit\n")
        if item in toDoList:
            new = input("what do you want to change it to?\n")
            index = toDoList.index(item)
            toDoList[index] = new
            print(f"'{item}' had been updated to '{new}'.")
    elif menu=="delete":
        toDoList = []
        print(f"{toDoList} has been deleted.")
    time.sleep(1)
    os.system('clear')
    

