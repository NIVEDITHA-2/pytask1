num=int(input("Enter the number:"))
s=0
i=1

temp=num
while temp!=0:
    rem=temp%10
    s=s*10+rem
    temp=int(temp/10)
temp=s
s=0
while temp!=0:
        rem=temp%10
        s=s+pow(rem,i)
        temp=int(temp/10)
        i=i+1
if s==num:
  print("Number is disarium")
else:

  print(" not a disarium number")



