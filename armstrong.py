n=int(input("Enter the number:"))
s=0
temp=n
while temp>0:
    r=temp%10
    s=s+r**3
    temp=temp//10
if s==n:
    print(n,"is armstrong number")
else:
    print(n,"is not armstrong")




