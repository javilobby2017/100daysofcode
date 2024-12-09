#print("If you put " , "\033[33m ", "nothing as the " , "\033[35m ", "end character ", "\033[32m ", "then you don\'t ", "\033[0m", "get odd gaps", sep="")

#turning the curser off 

import os, time

print('\033[?25l', end="")

for i in range(1,101):
    print(i)
    time.sleep(0.01)
    os.system('clear')

print('\033[?25h', end="")