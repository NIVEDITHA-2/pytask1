n=int(input("Enter a number:"))
a=5*n**2+4
b=5*n**2-4
flag=0
for i in range(1,a or b):
    if i**2==a or i**2==b:
        flag=1
if flag==1:
    print("is fibonacci")
else:
    print("not fibonacci")










