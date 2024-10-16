'''Exercise 3: Simple To-Do List
1. Create an Empty List: Start with an empty list called todo_list.
2. Define Functions:
    ○ A function add_task(task) that adds a task to the list.
    ○ A function show_tasks() that prints all tasks in the list.'''

todo_list = []

def add_task(task):
    todo_list.append(task)

def show_tasks():
    for task in todo_list:
        print(task)

add_task("Task2")
add_task("Task8")
add_task("Task4")
add_task("Task0")
add_task("Task11")

show_tasks()

