# Simple To-Do List App

tasks = []

def show_menu():
    print("\n=== TO-DO LIST ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task: ")
        tasks.append(task)
        print(" Task added successfully!")

    elif choice == '2':
        if len(tasks) == 0:
            print(" No tasks to show.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == '3':
        if len(tasks) == 0:
            print(" No tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                num = int(input("Enter task number to remove: "))
                removed = tasks.pop(num - 1)
                print(f" Task '{removed}' removed successfully!")
            except:
                print(" Invalid input. Please try again.")

    elif choice == '4':
        print("Exiting To-Do List. Have a great day!")
        break

    else:
        print(" Invalid choice! Please select between 1-4.")
