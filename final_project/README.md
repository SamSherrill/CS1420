# To Done: Focus on What Matters

A command-line productivity application for managing tasks organized by focus areas. Built as the final project for CS 1420 (Introduction to Computer Science).

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Design Decisions](#design-decisions)
- [Technical Requirements](#technical-requirements)
- [Testing](#testing)
- [Future Enhancements](#future-enhancements)

## 🎯 Overview

**To Done** is a CLI-based task management tool that helps users organize their tasks by "Focus Areas" (like School, Work, or Personal). Unlike traditional to-do lists, To Done encourages users to think about different areas of their life and manage tasks within those contexts.

The application features:
- **Two-level navigation system**: First select a focus area, then manage tasks within it
- **Persistent storage**: All data saved automatically to JSON when exiting
- **Clean, intuitive interface**: Simple menu-driven navigation with helpful prompts
- **Focus area management**: Create, rename, and organize focus areas as your life changes

## ✨ Features

### Core Functionality

1. **Focus Area Management**
   - View all focus areas with task counts (active and completed)
   - Create new focus areas (maximum 10 to maintain focus)
   - Rename existing focus areas (automatically updates all associated tasks)
   - Delete focus areas (with confirmation if tasks exist)
   - Warning system when approaching focus area limit (at 8+)
   - Default focus areas: Work, Personal (on first run)

2. **Task Management**
   - Add tasks with descriptive titles
   - View all tasks in a focus area (with completion status)
   - Mark tasks as complete (shown with [X] checkbox)
   - Delete tasks with confirmation prompt
   - **Keyboard shortcuts** for faster navigation (A/S/D/F keys)
   - **Quick actions**: Type "S1" to complete task 1, "D2" to delete task 2

3. **Data Persistence**
   - Automatic save on exit (graceful shutdown even with Ctrl+C)
   - JSON-based storage for human-readable data
   - Loads previous session automatically on startup
   - **Auto-cleanup**: Completed tasks are automatically removed on exit

4. **User Experience**
   - Built-in help system explaining all features
   - Clear visual feedback (✓ success, ✗ error, ⚠️ warnings)
   - Input validation and error handling
   - Task counts and completion statistics at a glance
   - Ergonomic keyboard shortcuts (A/S/D/F positioned for easy access)

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- No external dependencies required (uses only standard library)

### Quick Start

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/SamSherrill/CS1420.git
   cd CS1420/final_project
   ```

2. **Run the application**
   ```bash
   python todone.py
   ```

That's it! The app will create a `tasks.json` file in the same directory to store your data.

### Keyboard Shortcuts Quick Reference

**Main Menu:**
- `1-10` = Select focus area | `A` = Add area | `S` = Edit area | `D` = Delete area | `F` = Help | `G` = Exit

**Task Menu:**
- `A` = Add task | `S` = Complete task | `D` = Delete task | `F` = Back
- **Quick actions:** `S1` = Complete task 1 | `D2` = Delete task 2

> 💡 **Tip**: Keys A/S/D/F are positioned on the keyboard home row for easy access!

For more details, see [QUICKSTART.md](QUICKSTART.md).

## 📖 Usage

### Starting the Application

Run the main script:
```bash
python todone.py
```

### Navigation Flow

1. **Select a Focus Area**
   - Choose from existing focus areas (type the number)
   - Or press A to create a new focus area
   - Or press S to edit/rename an existing focus area
   - Or press D to delete a focus area
   - Or press F to view the help guide
   - Or press G to exit

2. **Manage Tasks**
   - Tasks are displayed immediately when you enter a focus area
   - Press A to add new tasks
   - Press S (or type S1, S2, etc.) to complete tasks
   - Press D (or type D1, D2, etc.) to delete tasks
   - Press F to return to focus area selection

3. **Exit**
   - Press G from the main menu
   - Or press Ctrl+C anywhere (graceful shutdown)
   - Completed tasks are automatically removed
   - All remaining tasks are saved

### Example Session

```
=== TO DONE: Focus on What Matters ===

YOUR FOCUS AREAS:
  1. Personal (2 active, 1/3 complete)
  2. Work (3 active, 0/3 complete)

OPTIONS:
  A. Create New Focus Area
  S. Edit Focus Area Name
  D. Delete Focus Area
  F. Help / How to Use
  G. Exit (Save & Quit)

Select an option (1-2 or A/S/D/F/G): 2

--- TASKS IN WORK ---
1. [ ] Download To Done CLI (Work)
2. [ ] Start using To Done (Work)
3. [X] Read documentation (Work)

OPTIONS:
  A. Add a New Task
  S. Complete a Task
  D. Delete a Task
  F. Back to Focus Areas

TIP: Type 'S1' to quickly complete task 1, or 'D2' to delete task 2

Enter your choice (A/S/D/F or S1, D2, etc.): S1
✓ Task 1 marked as complete!
```

## 📁 Project Structure

```
final_project/
├── todone.py           # Main application with menu system and UI
├── task.py             # Task class definition
├── task_manager.py     # TaskManager class with business logic
├── test_todone.py      # Automated test suite
├── README.md           # This file
├── Final Project Design.txt  # Original design document
└── tasks.json          # Data file (created on first run)
```

### Code Organization

- **`task.py`**: Defines the `Task` class representing individual tasks
  - Attributes: title, focus_area, is_complete
  - Methods: mark_complete(), __str__(), to_dict(), from_dict()

- **`task_manager.py`**: Defines the `TaskManager` class for managing collections
  - Manages tasks list and focus_areas set
  - Handles all CRUD operations
  - Implements JSON persistence

- **`todone.py`**: Main application logic
  - Two-level menu system
  - User input handling and validation
  - Display formatting and user feedback

## 🎨 Design Decisions

### Deviations from Original Design Document

The implementation differs from the original design in several key ways:

1. **Two-Level Menu System** (NEW)
   - **Original**: Single menu with all operations
   - **Implemented**: Focus area selection → Task management
   - **Rationale**: Better separation of concerns, clearer mental model for users

2. **Focus Area Management** (ENHANCED)
   - **Original**: Focus areas were just task attributes
   - **Implemented**: First-class entities with create/rename operations
   - **Rationale**: Focus areas change over time (e.g., graduating school, changing jobs)

3. **Completed Tasks Remain Visible** (CHANGED)
   - **Original**: Not specified
   - **Implemented**: Completed tasks stay in list with [X] marker
   - **Rationale**: Users can see their accomplishments and track history

4. **Default Focus Areas** (CHANGED)
   - **Original**: Empty on first run or School/Work/Personal
   - **Implemented**: Work and Personal only
   - **Rationale**: Most universally applicable; users can add School/Fitness/etc. as needed

5. **Task Counts in Focus Area Menu** (ADDED)
   - **Original**: Simple list of focus areas
   - **Implemented**: Shows active count and completion ratio
   - **Rationale**: Users can see at a glance where they need to focus

6. **Keyboard Shortcuts** (NEW)
   - **Original**: Numeric menu choices
   - **Implemented**: Letter-based shortcuts (A/S/D/F) and quick commands (S1, D2)
   - **Rationale**: Ergonomic positioning, faster workflow for power users

7. **Focus Area Limits** (NEW)
   - **Original**: Unlimited
   - **Implemented**: Maximum 10, warning at 8+
   - **Rationale**: Prevents overwhelming users; 7±2 is optimal for human categorization

8. **Auto-Cleanup on Exit** (NEW)
   - **Original**: Tasks remain indefinitely
   - **Implemented**: Completed tasks auto-removed when exiting
   - **Rationale**: Keeps focus on active work, encourages regular completion

9. **Delete Focus Area Feature** (NEW)
   - **Original**: Not specified
   - **Implemented**: Can delete focus areas with confirmation
   - **Rationale**: Life circumstances change; need to remove outdated areas

10. **Confirmation Prompts** (NEW)
    - **Original**: Immediate actions
    - **Implemented**: Confirms deletions showing impact
    - **Rationale**: Prevents accidental data loss

### Python Concepts Demonstrated

As required by the course rubric, this project demonstrates:

- **Object-Oriented Programming**: Two well-designed classes (Task, TaskManager)
- **Collections**: Lists for tasks, Sets for focus areas
- **Loops**: while loops for menu system, for loops for iterating collections
- **Conditionals**: if/elif/else for menu selection and validation
- **File I/O**: JSON serialization and deserialization
- **Error Handling**: try/except blocks for user input and file operations
- **Type Hints**: Modern Python type annotations throughout
- **Documentation**: Comprehensive docstrings in NumPy style

## 🔧 Technical Requirements

### Python Standard Library Modules Used

- `json`: For data persistence
- `typing`: For type hints (List, Set)
- `os`: For file existence checking in tests

### Class Diagram

```
┌─────────────────────┐
│       Task          │
├─────────────────────┤
│ - title: str        │
│ - focus_area: str   │
│ - is_complete: bool │
├─────────────────────┤
│ + mark_complete()   │
│ + to_dict()         │
│ + from_dict()       │
│ + __str__()         │
└─────────────────────┘
           ▲
           │ manages
           │
┌─────────────────────┐
│   TaskManager       │
├─────────────────────┤
│ - tasks: List[Task] │
│ - focus_areas: Set  │
│ - filename: str     │
├─────────────────────┤
│ + add_task()        │
│ + get_tasks()       │
│ + complete_task()   │
│ + delete_task()     │
│ + add_focus_area()  │
│ + rename_focus_area()│
│ + save_to_file()    │
│ + load_from_file()  │
└─────────────────────┘
```

## ✅ Testing

### Running the Test Suite

Execute the automated test suite:
```bash
python test_todone.py
```

The test suite validates:
- Task class creation and methods
- TaskManager CRUD operations
- Focus area management
- JSON persistence (save/load)
- Filter operations (completed vs active tasks)

All tests use assertions and provide clear output showing what's being tested.

### Manual Testing

For interactive testing, simply run the main application:
```bash
python todone.py
```

Try these scenarios:
1. Create a new focus area and add tasks to it
2. Complete some tasks and verify they show [X]
3. Exit and restart to verify persistence works
4. Rename a focus area and check that tasks moved correctly
5. Delete tasks and verify they're removed

## 🚀 Future Enhancements

Potential features for future versions:

1. **Due Dates**: Add date attributes and sort by urgency
2. **Priority Levels**: High/Medium/Low priority tags
3. **Filter by Status**: View only active or only completed tasks
4. **Search Functionality**: Search tasks by keywords
5. **Task Notes**: Add detailed descriptions to tasks
6. **Export Options**: Export to CSV or Markdown
7. **Statistics**: View productivity metrics and trends
8. **Archive System**: Move old completed tasks to archive
9. **Color Coding**: Use ANSI colors for better visual hierarchy
10. **Multi-file Support**: Separate JSON files per focus area

## 📝 License

MIT License - Feel free to use this code for learning purposes.

## 👤 Author

Samuel Sherrill, a Technology Management major at Utah Valley University  
GitHub: [@SamSherrill](https://github.com/SamSherrill)

## 🙏 Acknowledgments

- Implementation completed in Fall 2025 as part of CS 1420's final project
- A HUGE thank you to the course instructor for her patience with me!

---

**Note**: This project demonstrates proficiency in fundamental programming concepts including OOP, data structures, file I/O, and user interface design. The code follows Python best practices and is thoroughly documented for educational purposes.
