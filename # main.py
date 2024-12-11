# main.py
from task import Task
from file_handler import load_tasks, save_tasks
from utilities import validate_title, validate_deadline

def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        print(task)

def add_task(tasks):
    title = input("Enter task title: ")
    if not validate_title(title):
        print("Invalid title! Use 3-50 alphanumeric characters.")
        return

    description = input("Enter task description: ")

    deadline = input("Enter task deadline (YYYY-MM-DD): ")
    if not validate_deadline(deadline):
        print("Invalid deadline format! Use YYYY-MM-DD.")
        return

    task = Task(title, description, deadline)
    tasks.append(task)
    print("Task added successfully.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
