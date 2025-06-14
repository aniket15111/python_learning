def password_strength(p):
    is_up = False
    is_low = False
    is_sp = False
    is_digit = False

    if len(p) < 8:
        print("Password too short! Enter at least 8 characters.")
        return

    for ch in p:
        if ch==" ":
            print("You can not include spaces in password")
            return
        if ch.isupper():
            is_up = True
        elif ch.islower():
            is_low = True
        elif ch.isdigit():
            is_digit = True
        elif not ch.isalnum():  # Special character
            is_sp = True


    if all([is_up, is_low, is_digit, is_sp]):
        print("✅ Strong password!")
    else:
        print("❌ Weak password! Include:")
        if not is_up:
            print("- At least one UPPERCASE letter")
        if not is_low:
            print("- At least one lowercase letter")
        if not is_digit:
            print("- At least one number")
        if not is_sp:
            print("- At least one special character (!@# etc.)")



password=input("Enter password:")
password_strength(password)
