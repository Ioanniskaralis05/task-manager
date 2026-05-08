tasks = []

while True:
    print("\n--- Task Manager ---")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Show Tasks")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        task = input("Enter task to delete: ")
        if task in tasks:
            tasks.remove(task)
            print("Task deleted!")
        else:
            print("Task not found.")

    elif choice == "3":
        print("\nTasks:")
        for task in tasks:
            print("-", task)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")