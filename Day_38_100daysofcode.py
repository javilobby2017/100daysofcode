vowels = ["a", "e", "i", "o", "u"]


myString = input("Type something > ")
for letter in myString:
    if letter.lower() in vowels:
        print('\033[33m', end='') #yellow
    print(letter, end='')
    print('\033[0m', end='') #back to default

    #day 38 challenge ask user to type a senctence then any time they type an r will be red. and b will be blue