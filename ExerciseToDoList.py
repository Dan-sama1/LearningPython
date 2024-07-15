import os

File_Path = "D:\\DAN\\PATH\\ToDoList.txt"


def menu():
    print('--------------------')
    print("---- TO-DO LIST ----")
    print('--------------------')
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Complete")
    print("6. Remove Completed Tasks")
    print("7. Exit")


def load_task():
    if os.path.exists(File_Path):
        with open(File_Path, 'r') as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    return []


def save_task(tasks):
    with open(File_Path, 'w') as file:
        for task in tasks:
            file.write(task + '\n')


def add_task(tasks):
    print("---- ADD TASK ----")
    print("Enter task [0 to EXIT]:")
    task = input(">> ").strip()
    if task in tasks:
        print("Task already exists.")
    elif task == '0':
        return
    elif task == "":
        print("You cannot add a blank task, please try again.")
        add_task(tasks)
    else:
        tasks.append(f"[ ] | {task}")
        save_task(tasks)
        print("Task Added successfully")


def view_task(tasks):
    print("---- YOUR TASKS ----")
    if tasks:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("YOU HAVE NO TASKS TO DO :)")


def update_task(tasks):
    view_task(tasks)
    print("---- UPDATE TASKS ----")
    while True:
        try:
            print("Enter the task number to update [0 to EXIT]:")
            task_num = int(input(">> "))
            if 1 <= task_num <= len(tasks):
                print("Enter the new task description: ")
                new_task = input(">> ").strip()
                if new_task == '':
                    print("You cannot add a blank task, please try again.")
                    continue
                tasks[task_num-1] = f"[ ] | {new_task}"
                print("Task updated successfully...")
                input("Press ANY key to continue...")
                break
            elif task_num == 0:
                break
            else:
                print("Invalid task number, please try again.")
        except ValueError:
            print("Please enter a valid number.")


def delete_task(tasks):
    view_task(tasks)
    print("---- DELETE TASKS ----")
    while True:
        try:
            print("Enter the task number to delete [0 to EXIT]: ")
            task_num = input(">> ").strip()
            if task_num == 0 or task_num == '':
                print("Task deletion cancelled.")
                input("Press ANY key to continue...")
                break
            task_num = int(task_num)
            if 1 <= task_num <= len(tasks):
                while True:
                    print("Are you sure you want to DELETE this task? [Y/N]")
                    choice = input(">> ").strip().upper()
                    if choice == 'Y':
                        tasks.pop(task_num - 1)
                        save_task(tasks)
                        print("Task deleted successfully.")
                        input("Press ANY key to continue...")
                        break
                    elif choice == 'N' or choice == '':
                        print("Task deletion cancelled.")
                        break
                    else:
                        print("Invalid input, please try again.")
                break
            else:
                print("Invalid task number, please try again.")
        except ValueError:
            print("Please enter a valid number.")


def mark_complete(tasks):
    view_task(tasks)
    print("---- MARK TASKS ----")
    while True:
        try:
            print("Enter the task number to mark as complete [0 to EXIT]:")
            task_num = int(input(">> "))
            if 1 <= task_num <= len(tasks):
                task = tasks[task_num - 1]
                if task.startswith("[ ]"):
                    tasks[task_num - 1] = task.replace("[ ]", "[x]", 1)
                    save_task(tasks)
                    print("Task marked sa complete.")
                    input("Press ANY key to continue...")
                    break
                else:
                    print("The task is already complete.")
                    input("Press ANY key to continue...")
                    break
            elif task_num == 0:
                break
            else:
                print("Invalid task number, please try again.")
        except ValueError:
            print("Please enter a valid number.")


def remove_complete(tasks):
    view_task(tasks)
    print("---- REMOVE COMPLETED TASKS ----")
    while True:
        print("Are you sure you want to REMOVE the COMPLETED tasks? [Y/N]")
        choice = input(">> ").strip().upper()
        if choice == 'Y':
            tasks = [task for task in tasks if not task.startswith("[x]")]
            save_task(tasks)
            print("All completed tasks have been remove.")
            input("Press ANY key to continue...")
            return tasks
        elif choice == 'N' or choice == '':
            print("Task removal cancelled.")
            return tasks
        else:
            print("Invalid input, please try again.")


def clear(tasks):
    #HIDDEN
    print("---- DELETE ALL ----")
    while True:
        print("ARE YOU SURE YOU WANT TO CLEAR THE TO-DO LIST? [Y/N]")
        choice = input(">> ").upper()
        if choice == 'Y':
            tasks.clear()
            save_task(tasks)
            break
        elif choice == 'N':
            print("To-Do List deletion cancelled.")
            break
        else:
            print("Invalid input, please try again.")


def main():
    tasks = load_task()
    while True:
        menu()
        try:
            print("Enter your choice: ")
            choice = int(input(">> "))
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_task(tasks)
            elif choice == 3:
                update_task(tasks)
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                mark_complete(tasks)
            elif choice == 6:
                tasks = remove_complete(tasks)
            elif choice == 7:
                print("Thank you for using To-Do List application")
                input("Press ANY key to continue...")
                break
            elif choice == 8:
                clear(tasks)
            else:
                print("Invalid input, please try again.")
        except ValueError:
            print("Invalid input, please try again.")


if __name__ == '__main__':
    main()

