def build_profile():
    profile = {}
    while True:
        key = input("Enter field (or 'done' to finish): ")
        if key.lower() == 'done':
            break
        value = input(f"Enter value for '{key}': ")
        profile[key] = value
    return profile

# Build and show profile
user_profile = build_profile()
print("\nUser Profile:")
for k, v in user_profile.items():
    print(f"{k.capitalize()} : {v}")
