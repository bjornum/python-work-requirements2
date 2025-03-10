# Note: Alot of comments that may seem messy, but tried to explain my thought pattern through it.
## Can close each task, by clicking the number next to it :D

# Access the Operative System
import os

# Access the random module
import random

# Used to access JSON Module
import json

# Easier navigation between tasks, simply write task number and that task will trigger
task = input("Enter an Task Number: ")
task = int(task)

# Task 1 - File to List Converted
if(task == 1):
    print("You have chosen: Task 1 - File to List Converted")
    
    ## Helper to see what one can type
    print("test and example is two files that exists. ")

    ## Prompt the user for a filename without any extensions needed
    state_an_filename = input("Write a file name (do not add the extension behind it): ")

    ## A list of extensions that are allowed.
    possible_extensions = [".txt", ".csv", ".json", ".pdf"]

    ## Variable to store the file to read.
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
    print("You have chosen: Task 3 - Simple Class and Inheritance")

    ## Import of Person file with Class of Student
    from person import Student

    ## A default student - As stated in the task (Otherwise would create two inputs for this with age and name)
    ## Passing these 3 parameters down to said file
    my_student_details = Student("Bjorn", 38, "S12345")

    # Call the greet method from the person.py file
    my_student_details.greet()

    # Print the student_id
    print(f"Student ID: {my_student_details.student_id}")

# Task 4 - Math Quiz with Exception Handling
if(task == 4):
    print("You have chosen: Task 4 - Math Quiz with Exception Handling")

    # Generate two random integers
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)

    ## The correct answer, adding number_one and number_two together
    correct_answer = number_one + number_two

    ## User need to answer the math question
    user_input = input(f"What is {number_one} + {number_two}? ")

    try:
        ## Convertss the user answer to an integer
        user_answer = int(user_input)

        ## Checking if the answer is correct or not
        if user_answer == correct_answer:
            print("Correct! Well done.")
        else:
            print(f"Oops! The correct answer is {correct_answer}.")

    # If user types a non integer
    except ValueError:
        print("Invalid input! Please enter a number.")

# Task 5 - Directory Lister
if(task == 5):
    print("You have chosen: Task 5 - Directory Lister")

    ## Hints as i found it hard to figure out what i could write and how.
    print("Tip 1. Use / before the name of the directory.")
    print("Tip 2. Can see part of the directory in the terminal, where you run this task.")

    ## Asking the user to enter the path of the directory
    directory_path = input("Please enter the directory path: ")

    try:
        ## Looking for all files and directories in the path given by the user
        items = os.listdir(directory_path)
        
        ## Printing the items in a nicely way, each on a new line with a - in front
        print("\nItems in the directory:")
        for item in items:
            print(f"- {item}")

    ## Error: Directory not existing or not found.
    except FileNotFoundError:
        print("Error: The directory does not exist.")

    ## Error: Cannot access the directory due to not being accessible (lack of permissions)
    except PermissionError:
        print("Error: Permission denied. Cannot access the directory.")

    ## Error: If something else goes wrong, simply print the message
    except Exception as error:
        print(f"An error occurred: {error}")

# Task 6 - JSON Settings Handler
if(task == 6):
    print("You have chosen: Task 6 - JSON Settings Handler")

    ## Placing the Settings json into an variable
    SETTINGS_FILE = "settings.json"

    ## Default settings in case it does not exist
    default_settings = {
        "theme": "dark",
        "volume": 80
    }

    ## 1. Checking if the file exists or not.
    ## json.dump makes it to json format from a dictionary.
    ## indent 4, simply makes it so it breaks the line, and make it more readable.
    if not os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "w") as file:
            json.dump(default_settings, file, indent=4)

    try:
        ## 2. Reading what is already on the file
        ## json.load makes it from json to an dictionary.
        with open(SETTINGS_FILE, "r") as file:
            settings = json.load(file)
    
    ## File not found or in incorrect format. simply place the default settings in it.
    except (json.JSONDecodeError, FileNotFoundError):
        print("Error: Settings file is missing or corrupted. Resetting to defaults.")
        settings = default_settings
        with open(SETTINGS_FILE, "w") as file:
            json.dump(settings, file, indent=4)

    ## 3. File is there, so we print what values it currently have.
    print("\nCurrent Settings:")
    for key, value in settings.items():
        print(f"- {key}: {value}")

    ## 4. User then can decide which key to change
    setting_to_change = input("\nWhich setting would you like to change? ").strip()

    ## If key found in settings (read from the file), then ask user to add a new value to json key
    if setting_to_change in settings:
        new_value = input(f"Enter new value for {setting_to_change}: ").strip()

        ## Convert value type based on existing data type
        if isinstance(settings[setting_to_change], int):
            try:
                ## Convert input to integer if needed - the volume
                new_value = int(new_value)

            ## Error: Was expecting an number on volume
            except ValueError:
                print("Invalid input! Expected a number.")
                exit()

        # 5. Saving new changes to the dictionary.
        settings[setting_to_change] = new_value

        ## 6. Opens the settings.json file as writable.
        ## Converts it from dictionary to json format and put it in, in a nicely format.
        try:
            with open(SETTINGS_FILE, "w") as file:
                json.dump(settings, file, indent=4)
            print("Settings updated successfully!")

        except IOError:
            print("Error: Could not write to settings file.")

    else:
        print("Invalid setting! Please choose a valid option.")
        
# Task 7 - Scoped Variables Experiment
if(task == 7):
    print("You have chosen: Task 7 - Scoped Variables Experiment")

    epic_variable = "I am declared first, outside any of the scopes! woop!"

    ## First function with the first scoped variable inside
    def first_scoped_function():
        epic_variable = "First layer of scope, inside a function!"
        print(epic_variable)

        ## A function inside a function, with yet another scoped variable within.
        def second_scoped_function():
            epic_variable = "Scoped scoped. i am inside a function, inside a function!"
            print(epic_variable)

        second_scoped_function()

    ## Trigger the first Function and display the variable afterward.
    first_scoped_function()
    print(epic_variable)

# Task 8 - Simple Calculator Module
if(task == 8):
    print("You have chosen: Task 8 - Simple Calculator Module")
    print("For this one you will test my awesome calculator functions!")

    ## Imports the calculator.py file, with these 4 functionalities.
    import calculator

    

    # Allowed Operations to make
    allowed_operations = ['add', 'substract', 'multiply', 'divide']

    try:
        ## Ask user for an action and two numbers
        number_one = int(input("Write a number: "))
        operation = input("Write which action you wish to test out (add, substract, multiply or divide): ")

        # Check if operation is valid
        if operation not in allowed_operations:
            print(f"Invalid operation! Please choose from: {', '.join(allowed_operations)}")

        else:
            ## Next number if operation was valid
            number_two = int(input("Write another number: "))
            
            # To have the variable defined, and wont cause any error of it not being so later.
            result = None

            if(operation == 'add'):
                result = calculator.add(number_one, number_two)

            elif(operation == 'substract'):
                result = calculator.substract(number_one, number_two)

            elif(operation == 'multiply'):
                result = calculator.multiply(number_one, number_two)

            elif(operation == 'divide'):
                ## This one is special, as one cannot divide by 0
                try:
                    result = calculator.divide(number_one, number_two)
                except ZeroDivisionError as error:
                    print(f"Error: {error}")
           
            ## Print the results only if result is got a value other than the default None
            if result is not None:
                print(f"Result: {result}")

    # Triggers if user attempt to type something else than number
    except ValueError:
            print("Invalid input! Please enter numbers only.")

# Task 9 - File Filtering and Writing
if(task == 9):
    print("You have chosen: Task 9 - File Filtering and Writing")

    ## Helper to see what one can type
    print("Hint: You can choose between test and example for this one")

    ## Ask for filename input
    file_to_locate = input("Write the name of the file to inspect: ").strip()

    ## Allowed file extensions
    possible_extensions = [".txt", ".csv", ".json", ".pdf"]

    ## Variable to store the correct file path
    file_to_read = None

    ## Find the existing file with a valid extension
    for extension in possible_extensions:
        file_path = file_to_locate + extension
        if os.path.exists(file_path):
            file_to_read = file_path
            ## Stop checking after finding a valid file
            break 

    ## If no valid file was found
    if not file_to_read:
        print("Error: File not found with the allowed extensions!")
    else:
        print(f"File found: {file_to_read}")

        ## Ask for the keyword to filter by
        keyword_to_search_for = input("Next, write a keyword you wish to use (Hint: 'cat' is one that exists): ").strip()

        try:
            ## Read and filter the file
            with open(file_to_read, "r", encoding="utf-8") as file:
                matching_lines = [line for line in file if keyword_to_search_for in line]

            ## Write filtered results to a new file
            if matching_lines:
                with open("filtered.txt", "w", encoding="utf-8") as output_file:
                    output_file.writelines(matching_lines)
                print(f"Filtered lines saved to 'filtered.txt' ({len(matching_lines)} lines found).")
            else:
                print("No lines found containing the keyword.")

        except Exception as error:
            print(f"Error processing the file: {error}")

# Task 10 - Debugging Practice (Print and Try / Except)
if(task == 10):
    print("You have chosen: Task 10 - Debugging Practice (Print and Try / Except)")

    ## Tip for the user to test this task
    print("Tip: Enter some numbers, some words")

    ## Function that accepts bad user values, and will inform user what went wrong
    def sum_numbers():

        ## Ask for user input
        user_input = input("Enter numbers separated by spaces: ")

        ## Debugging print: Showing exactly what were typed
        print(f"Raw input: {user_input}")

        ## Splitting input into a list of strings
        number_strings = user_input.split()
        print(f"Split input into list: {number_strings}")

        ## Empty list to store valid numbers found
        numbers = []  

        for num in number_strings:
            try:
                ## Try converting to numbers
                converted = int(num)
                 ## Store valid numbers
                numbers.append(converted)
            except ValueError:
                print(f"Error: '{num}' is not a valid number and will be skipped.")

        ## Print converted list
        print(f"Converted numbers: {numbers}")

        ## Check if we have valid numbers before summing
        if numbers:
            return sum(numbers)
        else:
            return "No valid numbers were entered."
    ## Showing the total sum of the numbers
    print(f"Total sum: {sum_numbers()}")
