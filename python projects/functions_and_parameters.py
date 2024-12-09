#functions

def hello(name, age):
    print("hello "+ name + ", you are " + str(age) + " years old!")

hello("javi" , 31)

# a function can handle on or more perameters
# parameters and arguments
# parameters are passed by refrence

def change(value):
    value["name"] = "bob"

val = {"name":"javi"}
change(val)

print(val)

#using return statement in a function

def hello(name, age):
    print("Hello " + name + " , you are " + str(age) + "years old!")
    

hello("javi" , 31)

#difference between parameters and arguments
# we can also accept multible parameters

#more functions 

def change (value):
    value = 2

val = 1
change(val)

print(val)




