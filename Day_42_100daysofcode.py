beast = {"Name": None,"Type": None,"Special": None,"hp": None,"mp": None}

print("MockeBeast")
print()

for name, value in beast.items():
    beast[name] = input(f"{name}:\t ").strip().title()

if beast["Type"]=="Earth":
    print("\033[32m", end="")
elif beast["Type"]=="Fire":
    print("\033[31m", end="")
elif beast["Type"]=="Water":
    print("\033[34m", end="")
elif beast["Type"]=="Air":
    print("\033[37m", end="")
else:
    print("\033[33m", end="")

for name, value in beast.items():
    print(f"{name:<15}: {value}")