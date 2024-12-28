
myEvents = []

#preventing data loss underneth the array 

f = open("calendar.txt", "r")
myEvents = eval(f.read()) #function that makes text into a string
f.close()


def prettyPrint():
    print()
    for row in myEvents:
        print(f"{row[0] :^15} {row[1] :^15}")
    print()

while True:
    menu = input("1: Add, 2: Remove\n")
    if menu=="1":
        event = input("What event?: ").capitalize()
        date = input("what date?: ")
        row = [event, date]
        myEvents.append(row)
        prettyPrint()
    else:
        criteria = input("what event do you want to remove?: ").title()
        for row in myEvents:
            if criteria in row:
                myEvents.remove(row)
        prettyPrint()

    f = open("calendar.txt", "w")
    f.write(str(myEvents))
    f.close

    

