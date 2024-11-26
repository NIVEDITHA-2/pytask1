x=str(input("Enter the string:"))
length=len(x)
a=length-3
b=length+2
for i in range(1,6):
    if i==1 or i==5:
        print(f"+{"_"*b}+")
    else:
        print(f"|{" "*b}|")
        if i==3:
            print(f"|{x}{""*a}|")
