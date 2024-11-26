a=[5,-2,9,-4,-6,-1,7]
start=int(input("Enter the first number:"))
stop=int(input("Enter the last number:"))
for i in range(start,stop):
    if a[i]<0:
        print(a[i],end=" ")