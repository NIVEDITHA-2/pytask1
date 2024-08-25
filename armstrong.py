n=int(input("Enter the number:"))
s=0
temp=n
while n>0:
    r=n%10
    s=s+(r**3)
    n=n//10
if temp==s:
   print(temp,"is an armstrong")
else:
    print(temp,"is not an armstrong number")




