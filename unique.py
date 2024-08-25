x=input("Enter a string:")
flag = False
y = []
for i in x:
    if i not in y:
        y.append(i)
    else:
        flag = True
        break
if flag:
    print("The string is not unique")
else:
    print("The string is unique")

