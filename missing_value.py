first=int(input("input first number:"))
last=int(input("Enter the last number:"))
b=[]
for i in range(first,last):
    a=[1,2,3,4,9]
    if i not in a:
        b.append(i)
print(b)






