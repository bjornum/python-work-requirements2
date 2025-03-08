# Note: Alot of comments that may seem messy, but tried to explain my thought pattern through it.
## Can close each task, by clicking the number next to it :D

# To be able to interact with the Operative System. (checking if file exists)
import os

# Easier navigation between tasks, simply write task number and that task will trigger
task = input("Enter an Task Number: ")
task = int(task)

# Task 1 - File to List Converted
## Flow: User writes a filename, without adding the extension behind it.
## Then run the filename given, with one of the extensions added as "allowed" ones.
## If finding one, simply open it as read only, strip the lines, and show it.
if(task == 1):
    print("You have chosen: Task 1 - File to List Converted")
    
    ## Prompt the user for a filename without any extensions needed
    state_an_filename = input("Write a file name (do not add the extension behind it): ")

    ## A list of extensions that are allowed.
    possible_extensions = [".txt", ".csv", ".json", ".pdf"]

    ## An variable to store the file if it is found.
    file_to_read = None

    ## Checking if file exists,  and if so then the extension of file.
    for extension in possible_extensions:
        ## Checking if there is any file, with an extension matching or not.
        if os.path.exists(state_an_filename + extension):
            ## I found it, so i then try to see if i can run it without any errors.
            try:
                ## In the lesson of (IO), this was how it was done to open a file, as read only.
                with open(state_an_filename + extension, "r") as file_to_read:
                    ## Going through all the lines, and stripping it for Whitespaces
                    lines = [line.strip() for line in file_to_read.readlines()]
                    ## Shows the lines
                    print(lines)
            ## An error came, so instead of breaking it. displaying the error instead.
            except Exception as error:
                print(f"Error reading the file: {error}")
            ## Breaking the loop after the try / except have been ran.
            break
    ## No file was found
    else:
        print("Error: File not found.")


# Task 2 - Task List Manager
## Flow: User send the list and task written to the tasks file, as parameters.
## It then based on the function, either adds or removes the task to the list.
## Typing done simply ends the loop, completing the task
if(task == 2):
    print("You have chosen: Task 2 - Task List Manager")

    ## Importing tasks.py and its functions.  Note: writing tasks.py cause an error.
    from tasks import add_task, remove_task

    ## Will contain a list of tasks
    task_list = []
    
    ## Doing a while loop, as this will keep running until True is met
    while True:
        action = input("What would you like to do? (add/remove/done): ").strip().lower()

        ## Adds a task to the list
        if action == "add":
            task = input("Enter the task to add: ").strip()
            add_task(task_list, task)
            print("Updated task list:", task_list)

        ## Removes a task from the list
        elif action == "remove":
            task = input("Enter the task to remove: ").strip()
            remove_task(task_list, task)  # Calling the remove_task function from tasks.py
            print("Updated task list:", task_list)

        ## Stops the while loop, displays the items.
        elif action == "done":
            print("You have these items in your List: ", task_list)
            print("Goodbye!")
            ## Stops the Loop, by breaking it! Otherwise it never becomes False, and becomes an infinite loop...
            break

        ## User tries to type a different command
        else:
            print("Invalid input. Please enter 'add', 'remove', or 'done'.")

# Task 3 - Simple Class and Inheritance
if(task == 3):
    print("Welcome to task numbah 3")