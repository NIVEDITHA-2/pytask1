a=[1,2,3,4,5,6]
length=len(a)
temp=a[0]
a[0]=a[length-1]
a[length-1]=temp
print("the list after interchanging first and last element is:",a)