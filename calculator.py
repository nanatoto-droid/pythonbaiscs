num1=int(input("Enter first number: "))
num2=float(input("Enter second number: "))
operator=input("Enter  an operator (+,-,*,/): ")

# perform the calculation based on operator
if operator=="+":
    result=num1+num2
elif operator=="-":
    result=num1-num2
elif operator=="*":
    result=num1*num2
elif operator=="/":
    if num2 != 0:
        result=num1/num2
    else:
        result="Error!Division by zero"
else:
    result="Invalid operator!"
print(f"the result is :{result}")



