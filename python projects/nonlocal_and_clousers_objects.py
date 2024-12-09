#variable scope
#declaring a varable inside a function

#nested functions
def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word)

talk('I am going to buy the milk')

#non local vari
def count(): #outer function
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        print(count)
    
    increment()

count()    

#clousers
def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count
    return increment

increment = counter()

print(increment()) #1
print(increment())
print(increment())

#objects

age = 8

