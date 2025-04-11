"""
Actions:
    add - add a new task to the to-do list
    delete - delete a task from the to-do list
    list - list all tasks in the todo list
"""
tasks = []
def add_task():
    task = input("enter a new task:")
    tasks.append(task)
    print("Task added successfully.")

def view_task():
    if len(tasks) == 0:
        print("no tasks.")
    else:
        print("list of tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}.{task}")

def delete_task():
    if len(tasks) == 0:
        print("no tasks to delete.")
    else:
        print('Tasks:')
        for i,task in enumerate(tasks):
            print(f'{i+1}.{task}')
        choice = int(input('enter the task number to delete:'))
        if 0 < choice <= len(tasks):
            del tasks[choice-1]
            print('Task deleted successfully.')
        else:
            print('Invalid task number.')

def main():
    # Run the command-line to-do list application.

    while True:
        print('\n ------To-Do-List Application------')
        print("1, Add task")
        print("2. View task")
        print("3.Delete task")
        print("4.Quit")

        choice = int(input("enter your choice:"))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            print("Thank you for using the To-Do-List Application")
        else:
            print('Invalid Choice.Please try again')

if __name__ == "__main__":
    main()
