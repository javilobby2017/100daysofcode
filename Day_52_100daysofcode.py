import traceback

debugMode = False
myStuff = []
# two new constructs using try and except
try:
    f = open("Stuff.mine", "r")
    myStuff = eval(f.read())
    f.close()
except:
    print("ERROR: Unable to load")
    if debugMode:
        print(traceback)
for row in myStuff:
    print(row)