import os, time

beast = {}

def prettyPrint(beast_data):
    print()

    if beast_data["Type"]=="Earth":
        print("\033[32m", end="")
    elif beast_data["Type"]=="Fire":
        print("\033[31m", end="")
    elif beast_data["Type"]=="Water":
        print("\033[34m", end="")
    elif beast_data["Type"]=="Air":
        print("\033[37m", end="")
    else:
        print("\033[33m", end="")

    for name, value in beast.items():
        print(f"{name:<15}: {value}")
    print("\033[0m]", end="")

while True:
    print("add your beast!")
    name = input("Name > ").strip().title()
    type = input("Type > ").strip().title()
    special = input("special > ").strip().title()
    hp = int(input("Hp > "))
    mp = int(input("mp > "))
    beast[name] = {"Type": type,"Special": special,"hp": hp,"mp": mp}
    print("-----------")
    print()

    print(f"details for {name}")
    prettyPrint(beast[name])

    print("\nin current collection")
    for beast_name, beast_data in beast.items():
        print(f"\nBeast: {beast_name}")

    prettyPrint(beast_data)