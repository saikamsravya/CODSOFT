# TO-DO LIST APPLICATION
tasks = []
# ADD TASK
def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added successfully!\n")
# VIEW TASKS
def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.\n")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])
        print()
# UPDATE TASK
def update_task():
    view_tasks()
    if len(tasks) == 0:
        return
    try:
        number = int(input("Enter task number to update: "))
        if number >= 1 and number <= len(tasks):
            new_task = input("Enter new task: ")
            tasks[number - 1] = new_task
            print("Task updated successfully!\n")
        else:
            print("Invalid task number.\n")
    except:
        print("Please enter only numbers.\n")
# DELETE TASK
def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    try:
        number = int(input("Enter task number to delete: "))
        if number >= 1 and number <= len(tasks):
            removed = tasks.pop(number - 1)
            print("Deleted task:", removed)
            print()
        else:
            print("Invalid task number.\n")
    except:
        print("Please enter only numbers.\n")
# MAIN PROGRAM
while True:
    print("====== TO-DO LIST MENU ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Enter your choice: ")
    # ADD TASK
    if choice == "1":
        add_task()
    # VIEW TASKS
    elif choice == "2":
        view_tasks()
    # UPDATE TASK
    elif choice == "3":
        update_task()
    # DELETE TASK
    elif choice == "4":
        delete_task()
    # EXIT
    elif choice == "5":
        print("Thank you for using To-Do List App!")
        break
    else:
        print("Invalid choice. Please try again.\n")