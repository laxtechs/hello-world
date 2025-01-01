
# Simple Calculator in Python

def add(x,y):
    return x + y

def subtract(x,y):
    return x-y

def Multiply(x,y):
    return x*y

def division(x,y):
    return x/y

# input from user 

num1 = float(input("Enter first number"))
num2 = float(input("Enter second number"))
operation = input("choose operation (+,-,*,/): ")

if operation == "+":
    print(add(num1,num2))

elif operation == '-':
    print(subtract(num1,num2))

elif operation == '*':
    print(Multiply(num1,num2))

elif operation == '/':
    print(division(num1,num2))

else:
    print("Invalid Input")



