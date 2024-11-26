print("Enter the operation to be performed:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice=input()
if choice=="1":
    number1=int(input("enter the first number:"))
    number2=int(input("Enter the second number:"))
    print("The sum is",number1+number2)

elif choice=="2":
    number1=int(input("Enter the first number:"))
    number2=int(input("Enter the second number:"))
    print("The difference is",number1-number2)

elif choice == "3":
    number1 = int(input("Enter the first number:"))
    number2 = int(input("Enter the second number:"))
    print("The product is",number1 * number2)

elif choice=="4":
    number1 = int(input("Enter the first number:"))
    number2 = int(input("Enter the second number:"))
    print("The division is",number1 / number2)
else:
    print("Invalid entry")




