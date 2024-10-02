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

