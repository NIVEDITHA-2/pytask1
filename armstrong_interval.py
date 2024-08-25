lower=int(input("Enter the lower range :"))
upper=int(input("Enter the upper range:"))
for num in range(lower,upper+1):
    order=len(str(num))
    s=0
    temp=num
    while temp>0:
        r=temp%10
        s=s+r**order
        temp=temp//10
        if num==s:
            print(s,end=" ")




