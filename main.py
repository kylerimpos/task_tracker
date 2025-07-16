import json
import os

TASK_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as file:
        return json.load(file)
    
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)
    
def duplicate(title):
    tasks = load_tasks()
    for task in tasks:
        if task['title'].lower() == title.lower():
            return True
    return False

def add_task(title):
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "Status": "Not Started"
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{title}' added successfully.")

def list_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks were found.")
        return

    print("Task List:")
    for task in tasks:
        print(f"{task['id']} --- {task['title']} --- {task['Status']}")


def show_menu():
    print("\n🛠 Task Tracker")
    print("1. Add Task")ß
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Toggle Task Completion")
    print("6. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            title = input("Enter task title: ").strip()
            if title:
                if duplicate(title):
                    print("Task with this title already exists.")
                else:
                    add_task(title)
            else:
                print("Task title cannot be empty.")
        elif choice == '2':
            list_tasks()

if __name__ == "__main__":
    main()