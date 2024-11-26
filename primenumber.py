n=int(input("Enter a number:"))
flag=1
for i in range(2,n):
    if n%i==0:
        flag=0
        break
if flag==0:
    print(" not a prime number")
else:
    print(" prime number")












