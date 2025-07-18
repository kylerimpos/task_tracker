import json
import os
import time
import tabulate as tb

DATA_DIR = "data"
TASK_FILE = os.path.join(DATA_DIR, "tasks.json")

class TaskManager:
    def __init__(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(TASK_FILE):
            return []
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
        
    def save_tasks(self, tasks):
        with open(TASK_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)

    def duplicate(self, title: str) -> bool:
        tasks = self.load_tasks()

        for task in tasks:
            if task["title"] == title:
                print("Task with this title already exists.")
                return True
        return False
    
    def add_task(self, title: str):
        tasks = self.load_tasks()

        if self.duplicate(title):
            return
        
        task = {
            "id": len(tasks) + 1,
            "title": title,
            "status": "Not Started",
            "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        tasks.append(task)
        self.save_tasks(tasks)
        print(f"Tasks {title} added successfully.")

    def update_task(self, task_id: int, title: str):
        tasks = self.load_tasks()

        if not tasks:
            print("No tasks were found. Try adding one!")
            return

        if self.duplicate(title):
            return
        
        for task in tasks:
            if task["id"] == task_id:
                task["title"] = title
                task["updated_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
                print("Title updated successfully.")
                self.save_tasks(tasks)
                return
        
        print("Task not found.")

    def list_tasks(self):
        tasks = self.load_tasks()

        if not tasks:
            print("No tasks were found.")
            return
        
        print("\nTask List: ")

        print(tb.tabulate(tasks, headers="keys", tablefmt="grid"))

    def delete_task(self, task_id: int):
        tasks = self.load_tasks()

        if not tasks:
            print("No tasks were found.")
            return
        
        updated_tasks = []

        for task in tasks:
            if task["id"] != task_id:
                updated_tasks.append()
            else:
                print(f"{task['title']} deleted.")

        if len(updated_tasks) == len(tasks):
            print("Task not found.")
            return
        
        self.save_tasks(updated_tasks)

    def toggle_in_progress(self, task_id: int):
        tasks = self.load_tasks()
        
        if not tasks:
            print("No tasks were found. Try adding one!")
            return

        for task in tasks:
            if task['id'] == task_id:
                task['status'] = "In Progress"
                task['updated_at'] = time.strftime("%Y-%m-%d %H:%M:%S")
                self.save_tasks(tasks)
                print(f"{task['title']} now in progress.")
                return
        
        print("Task not found.")

    def toggle_complete(self, task_id: int):
        tasks = self.load_tasks()

        if not tasks:
            print("No tasks were found. Try adding one!")
            return
    
        for task in tasks:
            if task['id'] == task_id:
                task['status'] = "Completed"
                task['updated_at'] = time.strftime("%Y-%m-%d %H:%M:%S")
                self.save_tasks(tasks)
                print(f"{task['title']} now completed!")
                return
        
        print("Task not found.")
    

