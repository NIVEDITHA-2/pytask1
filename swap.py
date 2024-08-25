#swap with third variable
#before swapping
x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
temp=x
x=y
y=temp
#after swapping
print("value of x is:",x)
print("value of y is:",y)

#swap without third variable
#before swapping
x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
x,y=y,x
#after swapping
print("value of x is:",x)
print("value of y is:",y)
