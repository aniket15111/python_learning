import json
file_name="Day2/tasks.json"

def load_tasks():
    try:
        with open(file_name,'r')as file:
            return json.load(file)
    except FileNotFoundError:
        return{}
def save_tasks(task_list):
    with open(file_name,'w')as file:
        json.dump(task_list,file)


task_list = load_tasks()
print("📋 Welcome to the To-Do List App")
print("-------------------------------")

task_list = {}
while True:
    print("""
Choose an option:
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Exit
""")
    input_from_user = input("> ")

    if input_from_user == "1":
        task = input("Enter your task: ")
        if task in task_list:
            print("⚠️ Task already exists.")
        else:
            task_list[task] = "Not completed"
            save_tasks(task_list)
            print("✅ Task added!")

    elif input_from_user == "2":
        if not task_list:
            print("📭 No tasks to show.")
        else:
            print("\n🗒️ Your Tasks:")
            for i, (task, status) in enumerate(task_list.items(), start=1):
                checkbox = "[✔]" if status == "completed" else "[ ]"
                print(f"{i}. {checkbox} {task}")

    elif input_from_user == "3":
        if not task_list:
            print("⚠️ No tasks to mark.")
            continue
        print("\nWhich task do you want to mark as completed?")
        for task in task_list:
            print(f"- {task}")
        complete = input("> ")
        if complete in task_list:
            task_list[complete] = "completed"
            save_tasks(task_list)
            print(f"✅ '{complete}' marked as completed.")
        else:
            print("❌ Task not found.")

    elif input_from_user == "4":
        if not task_list:
            print("⚠️ No tasks to delete.")
            continue
        print("\nWhich task do you want to delete?")
        for task in task_list:
            print(f"- {task}")
        deleted_key = input("> ")
        if deleted_key in task_list:
            task_list.pop(deleted_key)
            save_tasks(task_list)
            print(f"🗑️ Task '{deleted_key}' deleted.")
        else:
            print("❌ Task not found.")

    elif input_from_user == "5":
        print("👋 Exiting To-Do List App. Have a productive day!")
        break

    else:
        print("⚠️ Invalid option, please choose 1–5.")
