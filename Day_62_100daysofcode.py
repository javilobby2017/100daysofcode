#oop object oriented programming
#idea or concept to create a tmeplate of how something is going to work

class animal:
    species = None
    name = None
    sound = None

    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound
    #new def here
    def talk(self):
        #use f string here
        print(f"""{self.name} says {self.sound}""")
#inherentence
class bird(animal):
    
    def __init__(self, color):
        self.name = "bird"
        self.species = "avion"
        self.sound = "tweet"
        self.color = color

polly = bird("green")
polly.talk()
print(polly.color)

dog = animal("Dog","Canine", "Woof")
dog.talk()

#this prints an instance of an object
cow = animal("cow","Bo Taurus", "moo")
cow.talk()