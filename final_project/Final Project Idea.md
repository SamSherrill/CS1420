# Final Project Idea

## Project Proposal: To Done CLI

### Project Overview

I propose to build "To Done," a productivity application designed to help users manage tasks and maintain focus. This will be a Command Line Interface (CLI) program written in Python. It will allow users to add tasks, view them by category (Focus Area), mark them as complete, and delete them. To ensure data is not lost when the program closes, the application will save all data to a JSON file and reload it upon launch.

### Meeting the Requirements

This project allows me to demonstrate all the required concepts from CS 1400/1410 within a scope I can manage effectively.

#### 1. OOP and Classes (15 points)

I will design the program using Object-Oriented principles to prevent code duplication.

* **Task Class**: This class will represent a single task object. It will hold data such as title, focus_area (category), and is_complete. It will include methods to toggle its completion status and format itself as a string for display.
* **TaskManager Class**: This class will handle the logic. It will contain the collection of tasks and methods to add_task, delete_task, save_to_file, and load_from_file.

#### 2. Collections and Loops (14 points each)

* **Collections**: The TaskManager will use a List to store the Task objects.
* **Loops**: The main program will run inside a while loop (the "game loop") that continuously asks the user for a command (Add, View, Complete, Exit) until they choose to quit. Loops will also be used to iterate through the list of tasks to display them or find a specific task to delete.

#### 3. Branches (14 points)

* **Conditionals**: If/Elif/Else statements will be used to handle the user's menu selection. Inside the logic, branches will check if a task exists before trying to delete it, preventing errors.

#### 4. Persistence (File I/O)

* I will use Python's built-in json module. When the program starts, it will read a .json file and convert the data back into Task objects. When the program ends, it will write the current list of objects back to the file.

