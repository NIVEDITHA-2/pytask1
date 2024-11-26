a=[10,7,25,14,5,9]
N=11
length=len(a)
product=1
for i in range(length):
    product=(product*a[i])%N
    i=i+1
print("the reminder of multiplication is:",product)



