import json


# Task 1: Task class
class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(data["title"], data["completed"])

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title}"


# Task 2: Task Manager class
class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    # Load tasks from file
    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return [Task.from_dict(task) for task in data]
        except FileNotFoundError:
            return []

    # Save tasks to file
    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=2)

    # Add task
    def add_task(self, title):
        self.tasks.append(Task(title))
        self.save_tasks()
        print("Task added successfully.")

    # View tasks
    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        print("\nYour Tasks:")
        print("-" * 30)
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    # Mark task as completed
    def complete_task(self, index):
        try:
            self.tasks[index].completed = True
            self.save_tasks()
            print("Task marked as completed.")
        except IndexError:
            print("Invalid task number.")

    # Delete task
    def delete_task(self, index):
        try:
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f"Deleted: {removed.title}")
        except IndexError:
            print("Invalid task number.")


# Task 3: CLI Menu
def menu():
    manager = TaskManager()

    while True:
        print("\n===== TASK MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            manager.view_tasks()
            try:
                index = int(input("Enter task number to complete: ")) - 1
                manager.complete_task(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            manager.view_tasks()
            try:
                index = int(input("Enter task number to delete: ")) - 1
                manager.delete_task(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


# Run program
if __name__ == "__main__":
    menu()