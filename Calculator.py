#simple calculator program
def calculate(num1, num2, operation):
#Get user input
    #Input two numbers
    num1 = float(input("Enter the first number"))
    num2 = float(input("Enter the second number"))
    #Input the operation
    operation = input("Enter the operation(+, -, *, /): ")

    #perform the operation
    if operation == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2 
        print(f"{num1} - {num2} = {result}")
    elif operation == "*":
         result = num1 * num2
         print(f"{num1} * {num2} = {result}")
    elif  operation == "/":
         if num2 !=0:
             result = num1 / num2
             print(f"{num1} / {num2} = {result}")
         else:
             print("Error: Division by zero is not allowed")
    else:
        print("Invalid operation.Please enter one of +, -, *, or / .")
