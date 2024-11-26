a=[1,0,2,3,0,4,5,0]
x=[]
y=[]
length=len(a)
for i in range(length):
    if a[i]==0:
        x.append (a[i])
        x.append(0)
    else:
        x.append(a[i])
length=len(a)
for i in range(0,length):
    y.append(x[i])
print(y)
