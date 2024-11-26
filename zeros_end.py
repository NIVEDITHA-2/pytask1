a=[5,1,2,3,0,1,0,0]
for i in a:
    if i ==0:
        a.remove(i)
        a.append(i)

print(a)