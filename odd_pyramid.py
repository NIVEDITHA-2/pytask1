n=int(input("Enter the term:"))
k=1
for i in range(0,n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(0,i+1):
        print(k,end=" ")
        k=k+2
    print()

