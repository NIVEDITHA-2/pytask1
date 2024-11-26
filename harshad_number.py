n=int(input("Enter a number:"))
temp=n
s=0
while temp>0:
    rem=temp%10
    s=s+rem
    temp=temp//10
#print(s)
temp=n
if temp%s==0:
    print(n,"is Harshad number")
else:
    print(n,"is not Harshad number")