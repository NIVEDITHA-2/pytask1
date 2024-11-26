x=input("Enter a string:")
x1=x.split(" ")
print(x1)
length=len(x1)
for i in range(length):
    if len(x1[i])%2==0:
        print(x1[i])

