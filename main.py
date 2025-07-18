from task_manager import TaskManager

def show_menu():
    print("\n🛠 Task Tracker")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Title")
    print("4. Delete Task")
    print("5. Toggle Task In Progress")
    print("6. Toggle Task Completed")
    print("7. Exit")

def main():



    manager = TaskManager()

    while True:
        show_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            title = input("Enter task title: ").strip()
            if title:
                manager.add_task(title)
            else:
                print("Task title cannot be empty.")

        elif choice == '2':
            manager.list_tasks()

        elif choice == '3':
            task_id = int(input("Enter task id to update: "))
            title = input("New title: ").strip()
            if title:
                manager.update_task(task_id, title)
            else:
                print("Task title cannot be empty.")

        elif choice == '4':
            task_id = int(input("Enter task id to delete: "))
            if task_id:
                manager.delete_task(task_id)
            else:
                print("Task id cannot be empty.")
        
        elif choice == '5':
            manager.list_tasks()

            task_id = int(input("\nEnter task id: "))
            if task_id:
                manager.toggle_in_progress(task_id)
            else:
                print("Task id cannot be empty.")

        elif choice == '6':
            manager.list_tasks()

            task_id = int(input("\nEnter task id: "))
            if task_id:
                manager.toggle_complete(task_id)
            else:
                print("Task id cannot be empty.")

        elif choice == '7':
            print("Exiting Task Tracker...")
            break
    
        else:
            print("Invalid choice. Enter 1 - 6.")
    
if __name__ == "__main__":
    main()