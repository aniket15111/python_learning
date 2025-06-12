num1 = float(input("🔢 Enter number 1: "))
num2 = float(input("🔢 Enter number 2: "))
operation = input("➕ Enter an operator (+, -, *, /): ")

if operation == '+':
    print(f"✅ Result: {num1} + {num2} = {num1 + num2}")
elif operation == '-':
    print(f"✅ Result: {num1} - {num2} = {num1 - num2}")
elif operation == '*':
    print(f"✅ Result: {num1} * {num2} = {num1 * num2}")
elif operation == '/':
    if num2 == 0:
        print("⚠️ Error: Division by zero is not allowed.")
    else:
        print(f"✅ Result: {num1} / {num2} = {num1 / num2}")
else:
    print("❌ Invalid operator. Please use +, -, *, or /.")
