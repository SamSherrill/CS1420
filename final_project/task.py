"""task.py

Task class for To Done CLI application.
Represents a single task with title, focus area, and completion status.
"""


class Task:
    """Represents a single task.

    Attributes
    ----------
    title : str
        Description of the task
    focus_area : str
        Category/focus area the task belongs to
    is_complete : bool
        Whether the task has been completed
    """

    def __init__(self, title: str, focus_area: str, is_complete: bool = False):
        """Initialize a new task.

        Parameters
        ----------
        title : str
            Description of the task
        focus_area : str
            Category/focus area for the task
        is_complete : bool, optional
            Initial completion status (default False)
        """
        self.title = title
        self.focus_area = focus_area
        self.is_complete = is_complete

    def mark_complete(self) -> None:
        """Mark this task as complete."""
        self.is_complete = True

    def __str__(self) -> str:
        """Return formatted string representation of the task.

        Returns
        -------
        str
            Formatted task string with checkbox and focus area
        """
        checkbox = "[X]" if self.is_complete else "[ ]"
        return f"{checkbox} {self.title} ({self.focus_area})"

    def to_dict(self) -> dict:
        """Convert task to dictionary for JSON serialization.

        Returns
        -------
        dict
            Dictionary representation of the task
        """
        return {
            "title": self.title,
            "focus_area": self.focus_area,
            "is_complete": self.is_complete,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Create a Task object from a dictionary.

        Parameters
        ----------
        data : dict
            Dictionary containing task data

        Returns
        -------
        Task
            New Task object created from the dictionary
        """
        return cls(
            title=data["title"],
            focus_area=data["focus_area"],
            is_complete=data.get("is_complete", False),
        )
