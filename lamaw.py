import os

File_Path = 'D:\\DAN\\PATH\\LAMAW.txt'


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
    print("7. Clear TO-DO LIST")
    print("8. Exit")


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
    existing_task = [t.split('|', 1)[1].strip() for t in tasks]
    if task in existing_task:
        print("Task already existing.")
    elif task == '0':
        return
    elif task == '':
        print("You cannot add a blank task, please try again.")
        add_task(tasks)
    else:
        tasks.append(f"[ ] | {task}")
        save_task(tasks)
        print("Task, added successfully.")


def view_task(tasks):
    print("---- TO-DO LIST ----")
    if tasks:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("You have no tasks to do :)")


def update_task(tasks):
    view_task(tasks)
    print("---- UPDATE TASKS ----")
    while True:
        try:
            print("Enter the task number to update [0 TO EXIT]:")
            task_num = input(">> ").strip()
            if task_num == '0' or "":
                break
            task_num = int(task_num)
            if 1 <= task_num <= len(tasks):
                print('------------------')
                while True:
                    print("Enter the new task description [0 TO EXIT]: ")
                    new_task = input(">> ").strip()
                    existing_task = [t.split('|', 1)[1].strip() for t in tasks]
                    if new_task in existing_task:
                        print("Task already existing.")
                    elif new_task == '':
                        print('You cannot add a blank task, please try again.')
                    elif new_task == '0':
                        break
                    else:
                        tasks[task_num - 1] = f"[ ] | {new_task}"
                        save_task(tasks)
                        print("Task updated successfully.")
                        break
                break
            else:
                print("Invalid input, please try again.")
        except ValueError:
            print("Invalid input, please try again.")


def remove_task(tasks):
    view_task(tasks)
    print('---- REMOVE TASKS ----')
    while True:
        try:
            print('Enter the task number to remove [0 TO EXIT]:')
            task_num = input(">> ").strip()
            if task_num == '0' or task_num == "":
                print("Task removal cancelled.")
                break
            task_num = int(task_num)
            if 1 <= task_num <= len(tasks):
                print("Are you sure you want to delete this task? [Y/N]")
                while True:
                    choice = input(">> ").upper()
                    if choice == 'Y':
                        tasks.pop(task_num - 1)
                        save_task(tasks)
                        print("task removed successfully.")
                        break
                    elif choice == 'N':
                        print("Task removal cancelled.")
                        input("Press ANY key to continue.")
                        break
                    else:
                        print("Invalid input, please try again.")
                break
            else:
                print("Invalid input, please try again.")
        except ValueError:
            print("Invalid input, please try again.")



def mark_done(tasks):
    view_task(tasks)
    print('---- MARK TASKS ----')
    while True:
        try:
            print("Enter the task number to update [0 TO EXIT]:")
            task_num = input(">> ").strip()
            if task_num == '0' or "":
                break
            task_num = int(task_num)
            task = tasks[task_num-1]
            if task.startswith('[ ]'):
                tasks[task_num - 1] = task.replace('[ ]', '[x]', 1)
                save_task(tasks)
                print("Task marked as complete.")
                input("Press ANY key to continue...")
                break
            else:
                print("The task is already complete.")
                input("Press ANY key to continue...")
                break
        except ValueError:
            print("Invalid input, please try again.")


def remove_completed(tasks):
    view_task(tasks)
    print('---- REMOVE COMPLETED TASKS ----')
    while True:
        print("Are you sure you want to REMOVE completed tasks? [Y/N]")
        choice = input(">> ").strip().upper()
        if choice == 'Y':
            tasks = [task for task in tasks if not task.startswith('[x]')]
            save_task(tasks)
            print("Completed tasks removed successfully.")
            input("Press ANY key to continue...")
            return tasks
        elif choice == 'N' or choice == '':
            print("Completed task removal cancelled.")
            input("Press ANY key to continue...")
            return tasks


def clear(tasks):
    view_task(tasks)
    print('---- CLEAR TO-DO LIST ----')
    while True:
        print("Are you sure you want to CLEAR your To-Do List? [Y/N]")
        choice = input('>> ').strip().upper()
        if choice == 'Y':
            tasks.clear()
            save_task(tasks)
            break
        elif choice == 'N' or choice == '':
            print("PROCESS CANCELLED.")
            input("Press ANY key to continue...")
            break


def main():
    tasks = load_task()
    while True:
        try:
            menu()
            print("Enter you choice")
            choice = int(input(">> "))
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_task(tasks)
            elif choice == 3:
                update_task(tasks)
            elif choice == 4:
                remove_task(tasks)
            elif choice == 5:
                mark_done(tasks)
            elif choice == 6:
                tasks = remove_completed(tasks)
            elif choice == 7:
                clear(tasks)
            elif choice == 8:
                print("THANKS FOR USING LAMAW")
                input("Press ANY key to continue...")
                break
        except ValueError:
            print("Invalid input, please try again.")

if __name__ == '__main__':
    main()