first=int(input("Enter the first number:"))
last=int(input("Enter the last number:"))
b=[]
n=9
for i in range(first,last):
    if i%n==0:
        b.append(i)
print(b)






