for i in range(7):
    for  j in range(7):
        if (j==0 or j==6) or ((j==i) and (i>0 and i<4)) or (i==1 and j==5) or (i==2 and j==4):
            print("*",end="")
        else:
            print(end=" ")
    print()