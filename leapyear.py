year=int(input("Enter the year:"))
if year%400==0 or year%4==0:
    print(year,"is a leapyear")
else:
    print(year,"is not a leapyear")