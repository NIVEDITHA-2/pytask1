n=int(input("Enter a number of terms"))
a,b=0,1
print(a,b,end=" ")
s=0
if n<=0:
    print("invalid number")
else:
    for i in range (1,n):
        s=a+b
        print(s,end=" ")
        a=b
        b=s



