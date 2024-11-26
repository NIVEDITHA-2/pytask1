a=[1,2,3,4,5]
s=1
for i in range(s):
    temp=a[0]
    for j in range(len(a)-1):
        a[j]=a[j+1]
    a[len(a)-1]=temp
print(a)
