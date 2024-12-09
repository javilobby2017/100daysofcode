print ("list Generator")

start = int(input("starting value:"))
end = int(input("end value:"))
increment = int(input("intervales:"))
if start > end:
    increment *= -1
for i in range(200, 300, 20):
    print(i)