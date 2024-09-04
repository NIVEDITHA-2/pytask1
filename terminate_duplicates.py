a=[1,3,5,2,6,5,7,4,2,1]
length=len(a)
list1=[]
for i in range(0,length):
    for j in range(i+1,length):
        if a[i]==a[j]:
            list1.append (a[j])
            #print(list1)
            x=set(a)
            y=set(list1) #convert in to set
            z=x-y #z=set(a)-set(list1)

print(list(z),end=" ") #convert the set again in to list


