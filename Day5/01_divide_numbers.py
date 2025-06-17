try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    divide = a / b
    print(f"Answer is: {divide}")
except ZeroDivisionError:
    print("❌ Error: Second number cannot be 0.")
except ValueError:
    print("❌ Error: Please enter valid integers.")
