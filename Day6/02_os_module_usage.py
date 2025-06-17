import os
for i in range(1,7):
    folder_name = f'Day{i}'
    if os.path.exists(folder_name):
        print(f"Contents of {folder_name}:")
        print(os.listdir(folder_name))
    else:
        print(f"{folder_name} not found")

print("Current dir:", os.getcwd())
