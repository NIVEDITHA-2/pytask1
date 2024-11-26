a=int(input("Enter the first number:"))
b=int(input("Enter the last number:"))
c=[]
for i in range(a,b):
    if i%2==0:
        c.append(i)
print(c,end=" ")