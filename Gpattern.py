for i in range(7):
    for j in range(6):
        if j==0 or (j==4 and (i!=1 and i!=2)) or((i==0 or i==6)and(j>0 and j<4))or(i==3 and (j==3 or j==5)):
            print("*",end="")
        else:
            print(end=" ")
    print()