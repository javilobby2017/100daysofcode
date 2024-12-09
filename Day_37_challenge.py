print("STAR WARS NAME GENERATOR")
#adding a split function
all = input("Enter you first name, last name, your moms maiden name, and the city you were born in: ").split()
#this will put the rows into an array

first = all[0].strip()
last = all[1].strip()
maiden = all[2].strip()
city = all[3].strip()


name = f"{first[:3].title()}{last[:2].lower()} {maiden[:2].title()}{city[-3:].lower()}"

print(f"Your Star Wars name is {name}")