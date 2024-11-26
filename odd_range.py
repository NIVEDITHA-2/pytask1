a=[1,2,3,6,7,9,11,12,15]
first=int(input("Enter the first element:"))
last=int(input("Enter the last element:"))
for i in range(first,last):
    if a[i]%2!=0:
        print(a[i],end=" ")



