a=[1,2,3,4,2,4,5,1,8,6,7,5]
length=len(a)
c=[]
for i in range(0,length):
    for j in range(i+1,length):
        if a[i]==a[j]:
            c.append(a[j])
print(c,end=" ")









