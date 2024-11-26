# x=[3,6,1,1,9,1]
# length=len(x)
# target=1
# i=0
# x.sort()
# print(x)
# a=int(input("Enter the target:"))
# for i in range(0,length):
#     if x[i]==target:
#         first_pos=1
#         last_pos=i+1
#         break
# print(x[0],x[i]+1)
arr=[1,2,2,2,2,3,4,7,8,8]

n=len(arr)
x=2
first=-1
last=-1
for i in range(n):
    if x!=arr[i]:
        continue
    if first==-1:
        first=i
    last=i
if first!=-1:
    print("first occurence=",first,"\n last occurence=",last)
else:
    print("not found")


