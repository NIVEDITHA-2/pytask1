n=int(input("Enter the digit:"))
s=0
while n>0:
    r=n%10
    s=int(s+r)
    n=n/10
print(s)



