my_list=[1,4,2,5,3,6,4,2,1]
frequency={}
for i in my_list:
    if i in frequency:
        frequency[i]=frequency[i]+1
    else:
        frequency[i]=1
print(frequency)
