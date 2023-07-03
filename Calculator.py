"""
CALCULATOR
"""
num1=int(input("Enter the first number: "))
num2=int(input("Enter the Second number: "))

Operator=input("Enter the Operator(+,-,*,/):")

""" Using if else condition """

if Operator=="+":
    print(num1+num2)

elif Operator=="-":
    print(num1-num2)

elif Operator=="*":
    print(num1*num2)

elif Operator=="/":
    print(num1/num2)

else:
    print("Invalid operator")


