#each row in a  dictionary has a key name and a key value 

#clue = {}

#def prettyPrint():
    #print()
    #for key, value in clue.items():
        #print(key, value)


#while True:
    #name = input("Name: ")
    #location = input("Location: ")
    #weapon = input("Weapon: ")
    #clue[name] = {"location": location, "weapon": weapon}
    #print(clue)

    #prettyPrint()

john = {"daysCompleted": 46, "streak": 22 }
janet = {"daysCompleted": 21, "streak": 21 }
erica = {"daysCompleted": 75, "streak": 6 }
courseProgress = {"John": john, "Janet": janet,"Erica": erica}

print(courseProgress["Erica"]["daysCompleted"])