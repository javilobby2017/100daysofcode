#before autosave create a backup folder and a random file name and save a copy of that file to the folder
import os
import shutil
import random
import string

myEvents = []
#leading exsisting events from file
try:
    with open ("calender.txt","r") as f:
        myEvents = eval(f.read())
except FileNotFoundError:
    print("calender.txt not found. Starting with an empty calendar.")

#function to create backup folder
def create_backup():
    backup_folder = "backup"
    #make sure bf exsits
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    #generating file name
    random_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    backup_file = os.path.join(backup_folder, f"challenge_backup_{random_suffix}.txt")

     # Copy the current file to the backup folder
    shutil.copy("calendar.txt", backup_file)
    print(f"Backup created: {backup_file}")


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

    # creating back up before overwriting file
    try:
        create_backup()
    except FileNotFoundError:
        print("No exsisting calendar.txt to backup.")

    f = open("calendar.txt", "w")
    f.write(str(myEvents))
    f.close

    

