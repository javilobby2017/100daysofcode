import datetime

#myDate = datetime.date(year=2022, month=12, day=7)
#print(myDate)

#today = datetime.date.today()
#print(today)

#day = int(input("Day: "))
#month = int(input("month: "))
#year = int(input("year: "))

#date = datetime.date(year, month, day)
#print(date)

#delta means the difference between two codes

#today = datetime.date.today()
#difference = datetime.timedelta(days=14)

#newDate = today + difference

#print(newDate)

today = datetime.date.today()

holiday = datetime.date(year=2025, month=2, day=20)

if holiday > today:
    print("coming soon")
elif holiday < today:
    print("go back")
else:
    print("holiday less gooo")

