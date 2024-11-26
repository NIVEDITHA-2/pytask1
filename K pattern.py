row=0
col=4
for i in range(7):
    for j in range (5):
        if j==0 or (i==j+2 and j>1):
            print("*",end="")
        elif (i==row and j==col):
            print("*",end=" ")
            row=row+1
            col=col-1
        else:
            print(end=" ")
    print()

