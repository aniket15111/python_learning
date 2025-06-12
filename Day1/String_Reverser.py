sentence = input("🔁 Enter a sentence to reverse: ").strip()

if sentence == "":
    print("⚠️ You entered an empty string.")
else:
    reversed_sentence = sentence[::-1]
    print(f"🔄 Reversed: {reversed_sentence}")
