n=int(input("Enter the no.of terms:"))
b=[]
for i in range(n):
    a=int(input("Enter the numbers:"))
    b.append(a)
first=int(input("Enter the first element:"))
last=int(input("Enter the last element:"))
for i in range(first,last):
    if b[i]%2==0:
        print(b[i],end=" ")


