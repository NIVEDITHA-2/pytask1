for i in range(1,101):
    temp=str(i)
    s=0
    for j in range(len(temp)):
        c=int(temp[j])
        s=s+c**(j+1)
        if s==i:
            print(s)

