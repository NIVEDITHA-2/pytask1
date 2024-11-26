num=int(input("Enter the number:"))
y=[]
for i in range(1,num+1):
    y.append(i)
list1=[num**2 for num in range(1,num+1) if num%2==0]
print(list1)