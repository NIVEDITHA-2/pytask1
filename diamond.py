n=int(input("Enter the number of terms:"))
for i in range(n):
    print(" "*(n-i-1)+"* "*(i+1))
for j in range(n-1,0,-1):
    print(" "*(n-j)+"* "*(j))
