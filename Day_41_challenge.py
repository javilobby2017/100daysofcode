website = {"name": None, "url": None, "desc": None, "rating": None }

for name, value in website.items():
    website[name] = input(f"{name}: ")

print()
for name, value in website.items():
    print(f"{name}: {value}")