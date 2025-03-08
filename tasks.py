## Part of Task 2: Task List Manager

# Add Task by taking two parameters, task_list and task to place in it
def add_task(task_list, task):
    task_list.append(task)

# Remove Task by running a try except, where i remove task if found, otherwise error given
def remove_task(task_list, task):
    try:
        task_list.remove(task)
    except ValueError:
        print(f"Task '{task}' not found in the list.")
