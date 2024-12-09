import os, time
listofEmail = []

def prettyPrint():
    os.system("clear")
    print("listofEmail")
    print()
    counter = 1
    for index in range(len(listofEmail)):
        print(f"{index}: {listofEmail[index]}")
    time.sleep(1)

def spam(max):
    for i in range(0,max):
        print(f"""Email {i+1}
Dear {listofEmail[i]}
It has come to our attention that you're missing out on the amazing Replit 100 days of code.""")
        time.sleep(1)
        os.system("clear")

while True:
    os.system("clear") #clear the screen at the start of each iteration
    print("Spammer Inc.")
    menu = input("1: add email\n2: remove email\n3: show emails\n4: get Spamming\n> ")
    if menu == "1":
        email = input("email >")
        listofEmail.append(email)
    elif menu== "2":
        email = input("email >")
        if email in listofEmail:
            listofEmail.remove(email)
    elif menu == "3":
        prettyPrint()
    elif menu =="4":
        spam(10)
    time.sleep(1)
    os.system("clear")
        