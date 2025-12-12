"""task_manager.py

TaskManager class for To Done CLI application.
Manages the collection of tasks and focus areas with JSON persistence.
"""

import json
from typing import List, Set
from task import Task


class TaskManager:
    """Manages tasks and focus areas with persistence.

    Attributes
    ----------
    tasks : List[Task]
        List of all Task objects
    focus_areas : Set[str]
        Set of focus area names
    filename : str
        Name of JSON file for persistence
    MAX_FOCUS_AREAS : int
        Maximum number of focus areas allowed
    """

    MAX_FOCUS_AREAS = 10

    def __init__(self, filename: str = "tasks.json"):
        """Initialize TaskManager and load existing data.

        Parameters
        ----------
        filename : str, optional
            JSON file name for persistence (default "tasks.json")
        """
        self.tasks: List[Task] = []
        self.focus_areas: Set[str] = set()
        self.filename = filename
        self.load_from_file()
        # Clean up any completed tasks from previous session
        cleaned = self.cleanup_completed_tasks()
        if cleaned > 0:
            self.save_to_file()  # Save immediately after cleanup

    def add_task(self, title: str, focus_area: str) -> None:
        """Create and add a new task.

        Parameters
        ----------
        title : str
            Task description
        focus_area : str
            Focus area for the task
        """
        task = Task(title, focus_area)
        self.tasks.append(task)
        self.focus_areas.add(focus_area)

    def get_tasks(self, focus_area: str = None, include_completed: bool = True) -> List[Task]:
        """Get tasks, optionally filtered by focus area.

        Parameters
        ----------
        focus_area : str, optional
            Filter tasks by this focus area (None for all tasks)
        include_completed : bool, optional
            Whether to include completed tasks (default True)

        Returns
        -------
        List[Task]
            List of tasks matching the criteria
        """
        filtered_tasks = self.tasks

        if focus_area:
            filtered_tasks = [t for t in filtered_tasks if t.focus_area == focus_area]

        if not include_completed:
            filtered_tasks = [t for t in filtered_tasks if not t.is_complete]

        return filtered_tasks

    def complete_task(self, index: int, focus_area: str = None) -> bool:
        """Mark a task as complete.

        Parameters
        ----------
        index : int
            Index of the task in the filtered list
        focus_area : str, optional
            Focus area to filter by

        Returns
        -------
        bool
            True if successful, False if index invalid
        """
        tasks = self.get_tasks(focus_area, include_completed=True)
        if 0 <= index < len(tasks):
            tasks[index].mark_complete()
            return True
        return False

    def delete_task(self, index: int, focus_area: str = None) -> bool:
        """Delete a task from the list.

        Parameters
        ----------
        index : int
            Index of the task in the filtered list
        focus_area : str, optional
            Focus area to filter by

        Returns
        -------
        bool
            True if successful, False if index invalid
        """
        tasks = self.get_tasks(focus_area, include_completed=True)
        if 0 <= index < len(tasks):
            task_to_delete = tasks[index]
            self.tasks.remove(task_to_delete)
            return True
        return False

    def add_focus_area(self, focus_area: str) -> tuple[bool, str]:
        """Add a new focus area.

        Parameters
        ----------
        focus_area : str
            Name of the focus area to add

        Returns
        -------
        tuple[bool, str]
            (success, message) - True with success message, or False with error message
        """
        if not focus_area:
            return False, "Focus area name cannot be empty"
        
        if focus_area in self.focus_areas:
            return False, f"Focus area '{focus_area}' already exists"
        
        if len(self.focus_areas) >= self.MAX_FOCUS_AREAS:
            return False, f"Maximum {self.MAX_FOCUS_AREAS} focus areas reached"
        
        self.focus_areas.add(focus_area)
        return True, f"Focus area '{focus_area}' created successfully!"
    
    def at_focus_area_limit(self) -> bool:
        """Check if at or near focus area limit.

        Returns
        -------
        bool
            True if at 80% or more of limit
        """
        return len(self.focus_areas) >= int(self.MAX_FOCUS_AREAS * 0.8)

    def rename_focus_area(self, old_name: str, new_name: str) -> bool:
        """Rename a focus area and update all associated tasks.

        Parameters
        ----------
        old_name : str
            Current name of the focus area
        new_name : str
            New name for the focus area

        Returns
        -------
        bool
            True if successful, False if old name doesn't exist or new name already exists
        """
        if old_name not in self.focus_areas or new_name in self.focus_areas:
            return False

        # Update all tasks with this focus area
        for task in self.tasks:
            if task.focus_area == old_name:
                task.focus_area = new_name

        # Update focus areas set
        self.focus_areas.remove(old_name)
        self.focus_areas.add(new_name)
        return True
    
    def delete_focus_area(self, focus_area: str) -> int:
        """Delete a focus area and all its associated tasks.

        Parameters
        ----------
        focus_area : str
            Name of the focus area to delete

        Returns
        -------
        int
            Number of tasks that were deleted with the focus area
        """
        if focus_area not in self.focus_areas:
            return 0
        
        # Count and remove tasks in this focus area
        tasks_to_remove = [t for t in self.tasks if t.focus_area == focus_area]
        deleted_count = len(tasks_to_remove)
        
        for task in tasks_to_remove:
            self.tasks.remove(task)
        
        # Remove the focus area
        self.focus_areas.remove(focus_area)
        
        return deleted_count
    
    def cleanup_completed_tasks(self) -> int:
        """Remove all completed tasks from the task list.

        Returns
        -------
        int
            Number of tasks that were removed
        """
        initial_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if not t.is_complete]
        return initial_count - len(self.tasks)

    def save_to_file(self) -> None:
        """Save tasks and focus areas to JSON file."""
        data = {
            "focus_areas": list(self.focus_areas),
            "tasks": [task.to_dict() for task in self.tasks],
        }
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=2)

    def load_from_file(self) -> None:
        """Load tasks and focus areas from JSON file."""
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.focus_areas = set(data.get("focus_areas", []))
                self.tasks = [Task.from_dict(task_data) for task_data in data.get("tasks", [])]
        except FileNotFoundError:
            # First run - start with default focus areas
            self.focus_areas = {"Work", "Personal"}
            self.tasks = []
        except json.JSONDecodeError:
            # Corrupted file - start fresh
            self.focus_areas = {"Work", "Personal"}
            self.tasks = []
