n=int(input("Enter a number:"))
temp=n
while temp>=10:
    s=0
    while temp>0:
        rem=temp%10
        s=s+(rem**2)
        temp=temp//10
    temp=s
    print("sum:",temp)
if temp==1:
    print(n,"is a Happy Number")
else:
    print(n,"is not Happy Number")


