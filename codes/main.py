import task_manager as tm  # Module import

tasks_loaded = tm.load_tasks_from_file("to_do_list.txt")  # File handling
completed_tasks_loaded = tm.load_completed_tasks_from_file("completed_tasks.txt")

if tasks_loaded:  # Conditional statement
    clear_existing_tasks = input("'Tasks' already exist. Do you want to clear them? (yes/no): ")  # User input
    if clear_existing_tasks.lower() == 'yes':
        tm.tasks = []  # List operations
        tm.save_tasks_to_file("to_do_list.txt")
        print("Existing 'tasks' cleared.")  # Print statement
    elif clear_existing_tasks.lower() == 'no':
        print("Existing 'tasks' kept.")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

if completed_tasks_loaded:
    clear_existing_completed_tasks = input("'Completed tasks' already exist. Do you want to clear them? (yes/no): ")
    if clear_existing_completed_tasks.lower() == 'yes':
        tm.completed_tasks = []
        tm.save_completed_tasks_to_file("completed_tasks.txt")
        print("Existing 'completed tasks' cleared.")
    else:
        print("Existing 'completed tasks' kept.")

while True:  # Loop
    print("\n----------------------------------------------------------\nTo-Do List Options:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. View completed tasks")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        task = input("Enter a task: ")
        tm.add_task(task)  # Function call
    elif choice == '2':
        tm.view_tasks()
    elif choice == '3':
        task_index = int(input("Enter the task number to mark as completed: "))  # Type conversion
        tm.complete_task(task_index)
    elif choice == '4':
        task_index = int(input("Enter the task number to delete: "))
        tm.delete_task(task_index)
    elif choice == '5':
        tm.view_completed_tasks()
    elif choice == '6':
        confirm_exit = input("Are you sure you want to exit? (yes/no): ")
        if confirm_exit.lower() == 'yes':
            erase_data = input("Do you want to erase data from the text files before exiting? (yes/no): ")
            if erase_data.lower() == 'yes':
                open("to_do_list.txt", 'w').close()
                open("completed_tasks.txt", 'w').close()
            print("Exiting To-Do List.")
            break  # Loop control
        elif confirm_exit.lower() == 'no':
            continue
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")
    else:
        print("Invalid choice. Please select a valid option.")

