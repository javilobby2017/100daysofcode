#name = input("What's your name?")
#if name.lower().strip() == "javi":
#    print("Hello Baldy!")
#else:
#    print("What a beautiful head of hair!")

mylist = []

def printList():
    print()
    for i in mylist:
        print(i)
    print()

while True:
    addItem = input("Item > ").strip().capitalize()
    if addItem not in mylist:
        mylist.append(addItem)
    printList()