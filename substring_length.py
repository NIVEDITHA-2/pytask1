b=input("Enter a substring")
length=len(b)
count=1
for i in range(length-1):
    if b[i]==b[i+1]:
        count=count-1
print(length)