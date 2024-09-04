a=[2,4,6,2,6,5,4,4,3,5,5]
count={}
for i in a:
    if i in count:
        count[i]=count[i]+1
    else:
        count[i]=1
for key, value in count.items():
 print(key, "=" , value)







