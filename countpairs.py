arr=[2,4,6,5,3,7]
target=int(input("Enter a target:"))
pairs=[]
arr.sort()
length=len(arr)
left=0
right=length-1
while left<=right:
    if arr[left]+arr[right]==target:
        pairs.append((arr[left],arr[right]))
        left=left+1
        right=right-1
    elif arr[left]+arr[right]>target:
        right=right-1
    else:left=left+1
print("sum pair of the target are:",pairs)











