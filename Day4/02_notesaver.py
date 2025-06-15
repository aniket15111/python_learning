from datetime import datetime

def save_note(note: str, filename: str = "notes.txt") -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"[{timestamp}] {note}\n"
    
    with open(filename, "a") as file:
        file.write(entry)
    print("✅ Note saved to", filename)

# Ask user for a note
user_note = input("Enter your note: ").strip()

if user_note:
    save_note(user_note)
else:
    print("⚠️ No note entered. Nothing saved.")
