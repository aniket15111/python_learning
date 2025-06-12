# formula weight in kg/height square in meters
# Underweight: Below 18.5.
# Healthy weight: 18.5 to 24.9.
# Overweight: 25.0 to 29.9.
# Obese: 30.0 and higher.

weight = float(input("⚖️ Enter your weight in kg: "))
height = float(input("📏 Enter your height in meters: "))

bmi = weight / (height ** 2)

print(f"🧮 Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("⚠️ You are underweight.")
elif bmi < 24.9:
    print("✅ You have a healthy weight.")
elif bmi < 29.9:
    print("⚠️ You are overweight.")
else:
    print("🚨 You are obese.")
