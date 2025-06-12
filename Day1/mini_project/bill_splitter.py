print("🧾 Welcome to the Bill Splitter!")

# 1. Take inputs
total = float(input("Enter the total bill amount: ₹"))
tip_percent = float(input("Enter the tip percentage: "))
people = int(input("Enter the number of people: "))

# 2. Calculations
tip = (tip_percent / 100) * total
total_bill = total + tip
per_person = total_bill / people

# 3. Output
print("\n🧮 Bill Summary:")
print(f"Tip Amount: ₹{tip:.2f}")
print(f"Total Amount (with Tip): ₹{total_bill:.2f}")
print(f"Each Person Pays: ₹{per_person:.2f}")
