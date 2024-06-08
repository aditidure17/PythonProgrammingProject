tasks = []  # List operations
completed_tasks = []  # List operations

def load_tasks_from_file(filename):  # Function definition
    try:  # Exception handling
        with open(filename, 'r') as file:  # File handling
            lines = file.readlines()
            if not lines:  # Conditional statement
                print("No previous 'tasks' found.")  # Print statement
                return False  # Return statement
            for line in lines:  # Loop
                tasks.append(line.strip())  # List operations
        return True
    except FileNotFoundError:
        print("No previous 'tasks' found.")
        return False

def load_completed_tasks_from_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if not lines:
                print("No 'completed tasks' found.")
                return False
            for line in lines:
                completed_tasks.append(line.strip())
        return True
    except FileNotFoundError:
        print("No 'completed tasks' found.")
        return False

def save_tasks_to_file(filename):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')  # String operations

def save_completed_tasks_to_file(filename):
    with open(filename, 'w') as file:
        for task in completed_tasks:
            file.write(task + '\n')

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added successfully!")  # Print statement
    save_tasks_to_file("to_do_list.txt")

def view_tasks():
    if tasks:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, 1):  # Loop with enumeration
            print(f"\t{i}. {task}")
    else:
        print("Your To-Do List is empty.")

def complete_task(task_index):
    if 0 < task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)  # List operations
        completed_tasks.append(completed_task)
        print(f"Task '{completed_task}' marked as completed!")
        save_tasks_to_file("to_do_list.txt")
        save_completed_tasks_to_file("completed_tasks.txt")
    else:
        print("Invalid task number.")

def delete_task(task_index):
    if 0 < task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        print(f"Task '{deleted_task}' deleted!")
        save_tasks_to_file("to_do_list.txt")
    else:
        print("Invalid task number.")

def view_completed_tasks():
    if completed_tasks:
        print("Completed Tasks:")
        for i, task in enumerate(completed_tasks, 1):
            print(f"\t{i}. {task}")
    else:
        print("No completed tasks yet.")

