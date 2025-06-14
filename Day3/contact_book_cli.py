import json

FILENAME = "contact_book.json"

# Save contacts to file
def save(a):
    with open(FILENAME, "w") as file:
        json.dump(a, file, indent=4)
        print("Contacts saved successfully ✅")

# Load contacts from file
def load():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No saved contacts found. Starting with an empty contact book.")
        return {}

# Main menu
def menu():
    a = load() or {}  # load existing or start with empty
    while True:
        print(f"\nTotal contacts: {len(a)}")
        try:
            option = int(input("""
# Menu:
# 1. Add Contact
# 2. View Contacts
# 3. Search by Name
# 4. Delete Contact
# 5. Exit
# > """))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        if option == 1:
            a.update(adding_info())
        elif option == 2:
            view_info(a)
        elif option == 3:
            search(a)
        elif option == 4:
            delete(a)
        elif option == 5:
            save(a)
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid option. Please choose from 1 to 5.")

# Add a new contact
def adding_info():
    a = {}
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    a[name] = {"email": email, "phone": phone}
    print(f"✅ Contact '{name}' added.")
    return a

# View all contacts
def view_info(a):
    if not a:
        print("📭 No contacts to display.")
        return
    for i, (j, k) in enumerate(a.items(), start=1):
        print("--------------------------------")
        print(f"{i}. {j}")
        print(f"    Phone number: {k['phone']}")
        print(f"    E-mail: {k['email']}")

# Search contact by name
def search(a):
    name = input("Enter name to search: ").strip()
    if name in a:
        print(f"📞 Phone number: {a[name]['phone']}")
        print(f"📧 E-mail: {a[name]['email']}")
    else:
        print("❌ Contact not found.")

# Delete a contact
def delete(a):
    name = input("Enter name to delete: ").strip()
    if name in a:
        confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").lower()
        if confirm == 'y':
            a.pop(name)
            print(f"🗑️ Contact '{name}' deleted.")
        else:
            print("Deletion canceled.")
    else:
        print("❌ Contact not found.")

# Entry point
print("""
----------------------
📒 Welcome to My Log Book
----------------------""")
menu()
