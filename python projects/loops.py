#loops
#while loops and define by using the keyword while

condition = True
while condition == True:
    print("The condition is True")
    condition = False

# exampile of while loop w/t exit

exit = "no"
while exit == "no":
  animal = input("What animal do you want?: ")
  if animal == "cow":
    print("A cow goes moo.")
  elif animal == "dog":
    print("A dog goes woof.")
  elif animal == "cat":
    print("A cat goes meow.")
  elif animal == "sheep":
    print("A sheep goes baa.")
  else:
    print("I dont know that one. Plz try again.")  
  exit = input("Do you want to exit?: ")

# for will execute a block for a pre determind amount of time. 

items = [1,2,3,4]
for item in items:
    print(item)
# using the range funticon with for loop will return a list

#while loops with lyrics excersise
counter = 1
while True:
  lyrics = input("Never going to ______ you up. ")
  if lyrics == "put":
    print("Nope, try again.")
    counter +=1
  if lyrics == "give":
    print("Well done! It only took you", counter, "attempts.")
    break
  print("Thanks for playing!")

#for loop loan calculator example with round
print("loan calculator")

total = 1000
apr = 0.05
for total in range(10):
  total += (total*apr)
  print("Year", total+1, "is", round(total,2))