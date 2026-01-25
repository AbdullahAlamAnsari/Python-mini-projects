a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))


c = (input("Enter the operator: "))
result = 0
if(c is "+"):
    result = a + b
elif(c is "-"):
    result = a - b
elif(c is "*"):
    result = a * b
elif(c is "/"):
    result = a / b
else:
    print("Invalid operator")

print(f"Result: ",result)