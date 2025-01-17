import datetime

today = datetime.date.today()

print("Event Countdown")

day = int(input("Day: "))
month = int(input("month: "))
year = int(input("year: "))

event = datetime.date(year, month, day)

difference = event - today
difference = difference.days


if difference >0:
    print(difference)
elif difference < 0:
    print("you missed it")
else:
    print("event less gooo")
