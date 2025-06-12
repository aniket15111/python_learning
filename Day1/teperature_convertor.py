temp = float(input("🌡️ Enter the temperature: "))
unit = input("📏 Is the temperature in Celsius (C) or Fahrenheit (F)? ").strip().upper()

if unit == 'C':
    f = (temp * 9/5) + 32
    print(f"✅ {temp}°C is equal to {f:.2f}°F")
elif unit == 'F':
    c = (temp - 32) * 5/9
    print(f"✅ {temp}°F is equal to {c:.2f}°C")
else:
    print("❌ Invalid unit. Please enter 'C' or 'F'.")
