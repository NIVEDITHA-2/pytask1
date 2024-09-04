a={'a','e','i','o','u'}
A={'A','E','I','O','U'}
b=input("Enter a string:")
c=set(b)
#output=a&set(b)
#print(output)
output1=A&set(b)
print(output1)
if output1==A:
    print("string accepted")
else:
    print("string not accepted")

