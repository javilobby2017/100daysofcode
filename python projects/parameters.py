def whichCake(ingredient, base, coating):#adding more arguments
    if ingredient == "chocolate":
        print("mmm, chocolate cake is amazing")
    elif ingredient == "brocolli":
        print("you what mate?")
    else:
        print("yeah, that's great I suppose...")
    print("so you want a", ingredient, "cake on a", base, "base with", coating,"on top?")
#inputing other arguments 
userIngredient = input("name an ingredient: ")
userBase = input("Name a type of base: ")
userCoating = input("fave cake topping: ")
#calling the subroutine
whichCake("carrot","biscuit","icing")
