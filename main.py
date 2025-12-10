import os

FILENAME = "TaskData.txt"

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        counter = 1
        for task in tasks:
            file.write(f"{counter} {task}\n")
            counter += 1

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    tasks = []
    with open(FILENAME, "r") as file:
        for line in file:
            parts = line.strip().split(" ", 1)
            if len(parts) == 2:
                task_text = parts[1]  # ignore the number
                tasks.append(task_text)
    return tasks


def menu():
    print("To Do List")
    print("1. View all current taks")
    print("2. Add a new task")
    print("3. Delete a task")
    print("4. Quit")

tasks = load_tasks()

while True:
    menu()
    choice = input("Please select one of the four options.");

    if choice == "1":
        print("\nTasks:")
        if tasks:
            counter = 1
            for task in tasks:
                print(f"{counter}. {task}")
                counter += 1
            else:
                print("No current tasks.")
        
    elif choice == "2":
        new_task = input("Enter task: ")
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"Task added: {new_task}.")

    elif choice == "3":
        task_number = input("Choose the number of the task you would like to delete.")
        if not tasks:
            print("There are no tasks to delete.")

        if task_number.isdigit():
            task_number = int(task_number)
            if 1 <= task_number <= len(tasks):
                removed = tasks.pop(task_number - 1)
                save_tasks(tasks)
                print(f"Removed: {removed}")
            else:
                print("Invalid number.")
        else:
            print("Please enter a number")

    elif choice == "4":
        print("Goodbye.")

    else:
        print("Invalid input.")
