def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
op = input("Enter the operation you want to perform (+, -, *, /): ")

if op == "+":
    print("Result:", add(a, b))
elif op == "-":
    print("Result:", sub(a, b))
elif op == "*":
    print("Result:", mul(a, b))
elif op == "/":
    print("Result:", div(a, b))
else:
    print("Invalid operation")
