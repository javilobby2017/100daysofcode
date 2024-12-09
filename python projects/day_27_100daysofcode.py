print ("Create a character")

def healthstat():
    import random
    value1 = random.randint(1,6)
    value2 = random.randint(1,12)
    health = (((value1*value2)/2)+12)
    return str(health)
def strengthstat():
    import random
    value1 = random.randint(1,6)
    value2 = random.randint(1,12)
    strength = (((value1*value2)/2)+12)
    return str(strength)

character = ("yes")

while character == "yes":
    character = input("name your character")
    characterType = input("character type(necromance,hunter,barbarian, other): ")
    print("Health: " + healthstat())
    print("Strength: " + strengthstat())
    print()
    character = input("build another character? ").lower