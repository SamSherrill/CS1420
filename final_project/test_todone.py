"""test_todone.py

Comprehensive test suite for To Done functionality.
Tests all core features, edge cases, and error handling.
"""

from task import Task
from task_manager import TaskManager
import os
import json


def test_task_class():
    """Test Task class functionality."""
    print("Testing Task class...")

    # Create task
    task = Task("Finish project", "Work")
    assert task.title == "Finish project"
    assert task.focus_area == "Work"
    assert task.is_complete == False
    print("✓ Task creation works")

    # Create task with completion status
    completed_task = Task("Done task", "Personal", is_complete=True)
    assert completed_task.is_complete == True
    print("✓ Task creation with is_complete works")

    # Mark complete
    task.mark_complete()
    assert task.is_complete == True
    print("✓ Mark complete works")

    # String representation - incomplete
    incomplete = Task("Buy milk", "Personal")
    task_str = str(incomplete)
    assert "[ ]" in task_str
    assert "Buy milk" in task_str
    assert "Personal" in task_str
    print("✓ String representation (incomplete) works")

    # String representation - complete
    complete = Task("Send email", "Work", is_complete=True)
    task_str = str(complete)
    assert "[X]" in task_str
    assert "Send email" in task_str
    print("✓ String representation (complete) works")

    # to_dict
    task_dict = task.to_dict()
    assert task_dict["title"] == "Finish project"
    assert task_dict["focus_area"] == "Work"
    assert task_dict["is_complete"] == True
    print("✓ to_dict works")

    # from_dict
    new_task = Task.from_dict(task_dict)
    assert new_task.title == "Finish project"
    assert new_task.focus_area == "Work"
    assert new_task.is_complete == True
    print("✓ from_dict works")

    # from_dict without is_complete (default to False)
    minimal_dict = {"title": "Test", "focus_area": "Work"}
    task_from_minimal = Task.from_dict(minimal_dict)
    assert task_from_minimal.is_complete == False
    print("✓ from_dict with missing is_complete defaults correctly")

    print("✅ All Task class tests passed!\n")


def test_task_manager():
    """Test TaskManager functionality."""
    print("Testing TaskManager class...")

    # Clean up test file if it exists
    test_file = "test_tasks.json"
    if os.path.exists(test_file):
        os.remove(test_file)

    # Test initialization with new file
    manager = TaskManager(test_file)
    print("✓ TaskManager initialization works")

    # Check default focus areas
    assert "Work" in manager.focus_areas
    assert "Personal" in manager.focus_areas
    assert len(manager.focus_areas) == 2
    print("✓ Default focus areas created correctly")

    # Test empty tasks on startup
    assert len(manager.tasks) == 0
    print("✓ Empty tasks list on first run")

    # Add task
    manager.add_task("Complete assignment", "Personal")
    tasks = manager.get_tasks("Personal")
    assert len(tasks) == 1
    assert tasks[0].title == "Complete assignment"
    assert tasks[0].focus_area == "Personal"
    print("✓ Add task works")

    # Add multiple tasks to same area
    manager.add_task("Buy groceries", "Personal")
    manager.add_task("Call dentist", "Personal")
    personal_tasks = manager.get_tasks("Personal")
    assert len(personal_tasks) == 3
    print("✓ Multiple tasks in same area works")

    # Add focus area
    success, message = manager.add_focus_area("Fitness")
    assert success == True
    assert "Fitness" in manager.focus_areas
    assert "created successfully" in message
    print("✓ Add focus area works")

    # Add duplicate focus area
    success, message = manager.add_focus_area("Fitness")
    assert success == False
    assert "already exists" in message
    print("✓ Duplicate focus area prevention works")

    # Add empty focus area name
    success, message = manager.add_focus_area("")
    assert success == False
    assert "cannot be empty" in message
    print("✓ Empty focus area name rejected")

    # Test focus area limit
    for i in range(7):  # Add 7 more (already have 3 = 10 total, at limit)
        manager.add_focus_area(f"Area{i}")
    
    success, message = manager.add_focus_area("OneMoreArea")
    assert success == False
    assert "Maximum" in message
    assert str(manager.MAX_FOCUS_AREAS) in message
    print("✓ Focus area limit enforcement works")

    # Test at_focus_area_limit warning
    assert manager.at_focus_area_limit() == True
    print("✓ Focus area limit warning detection works")

    # Remove some areas to continue testing
    manager.delete_focus_area("Area0")
    manager.delete_focus_area("Area1")

    # Get tasks by focus area
    manager.add_task("Go to gym", "Fitness")
    manager.add_task("Run 5K", "Fitness")
    fitness_tasks = manager.get_tasks("Fitness")
    assert len(fitness_tasks) == 2
    personal_tasks = manager.get_tasks("Personal")
    assert len(personal_tasks) == 3
    print("✓ Get tasks by focus area works")

    # Get all tasks (no filter)
    all_tasks = manager.get_tasks()
    assert len(all_tasks) >= 5
    print("✓ Get all tasks without filter works")

    # Complete task
    result = manager.complete_task(0, "Personal")
    assert result == True
    assert manager.get_tasks("Personal")[0].is_complete == True
    print("✓ Complete task works")

    # Try to complete invalid task index
    result = manager.complete_task(999, "Personal")
    assert result == False
    print("✓ Invalid complete task index handled")

    # Get tasks without completed
    active_tasks = manager.get_tasks("Personal", include_completed=False)
    assert len(active_tasks) == 2  # 3 total - 1 completed
    print("✓ Filter completed tasks works")

    # Get tasks including completed
    all_personal = manager.get_tasks("Personal", include_completed=True)
    assert len(all_personal) == 3
    print("✓ Include completed tasks works")

    # Cleanup completed tasks
    removed = manager.cleanup_completed_tasks()
    assert removed == 1
    assert len(manager.get_tasks("Personal")) == 2
    print("✓ Cleanup completed tasks works")

    # Cleanup when no completed tasks exist
    removed_again = manager.cleanup_completed_tasks()
    assert removed_again == 0
    print("✓ Cleanup with no completed tasks works")

    # Rename focus area
    manager.add_task("Another fitness task", "Fitness")
    result = manager.rename_focus_area("Fitness", "Health")
    assert result == True
    assert "Health" in manager.focus_areas
    assert "Fitness" not in manager.focus_areas
    health_tasks = manager.get_tasks("Health")
    assert len(health_tasks) == 3
    # Verify all tasks were updated
    for task in health_tasks:
        assert task.focus_area == "Health"
    print("✓ Rename focus area works")

    # Try to rename to existing focus area
    result = manager.rename_focus_area("Health", "Personal")
    assert result == False
    print("✓ Rename to existing focus area prevented")

    # Try to rename non-existent focus area
    result = manager.rename_focus_area("NonExistent", "NewName")
    assert result == False
    print("✓ Rename non-existent focus area handled")

    # Delete task
    initial_count = len(manager.get_tasks("Health"))
    result = manager.delete_task(0, "Health")
    assert result == True
    assert len(manager.get_tasks("Health")) == initial_count - 1
    print("✓ Delete task works")

    # Try to delete invalid task index
    result = manager.delete_task(999, "Health")
    assert result == False
    print("✓ Invalid delete task index handled")

    # Delete focus area with tasks
    task_count = len(manager.get_tasks("Health"))
    assert task_count > 0  # Make sure there are tasks
    deleted = manager.delete_focus_area("Health")
    assert deleted == task_count
    assert "Health" not in manager.focus_areas
    assert len(manager.get_tasks("Health")) == 0
    print("✓ Delete focus area with tasks works")

    # Delete empty focus area
    manager.add_focus_area("EmptyArea")
    deleted = manager.delete_focus_area("EmptyArea")
    assert deleted == 0
    assert "EmptyArea" not in manager.focus_areas
    print("✓ Delete empty focus area works")

    # Try to delete non-existent focus area
    deleted = manager.delete_focus_area("NonExistent")
    assert deleted == 0
    print("✓ Delete non-existent focus area handled")

    # Save to file
    manager.save_to_file()
    assert os.path.exists(test_file)
    print("✓ Save to file works")

    # Verify JSON structure
    with open(test_file, 'r') as f:
        data = json.load(f)
        assert "focus_areas" in data
        assert "tasks" in data
        assert isinstance(data["focus_areas"], list)
        assert isinstance(data["tasks"], list)
    print("✓ JSON file structure is correct")

    # Load from file in new manager
    new_manager = TaskManager(test_file)
    assert "Work" in new_manager.focus_areas
    assert "Personal" in new_manager.focus_areas
    print("✓ Load from file works")

    # Verify loaded data matches
    original_areas = sorted(manager.focus_areas)
    loaded_areas = sorted(new_manager.focus_areas)
    assert original_areas == loaded_areas
    print("✓ Loaded focus areas match saved data")

    # Test startup cleanup of completed tasks
    # Add and complete some tasks, save, then reload
    test_file2 = "test_cleanup.json"
    cleanup_manager = TaskManager(test_file2)
    cleanup_manager.add_task("Task 1", "Work")
    cleanup_manager.add_task("Task 2", "Work")
    cleanup_manager.complete_task(0, "Work")
    cleanup_manager.save_to_file()
    
    # Create new manager - should cleanup on load
    reloaded = TaskManager(test_file2)
    work_tasks = reloaded.get_tasks("Work")
    # Should only have 1 task (completed one was cleaned up)
    assert len(work_tasks) == 1
    assert not work_tasks[0].is_complete
    print("✓ Startup cleanup of completed tasks works")

    # Clean up test files
    os.remove(test_file)
    os.remove(test_file2)

    print("✅ All TaskManager tests passed!\n")


if __name__ == "__main__":
    print("=" * 60)
    print("RUNNING TO DONE TESTS")
    print("=" * 60 + "\n")

    test_task_class()
    test_task_manager()

    print("=" * 60)
    print("🎉 ALL TESTS PASSED! 🎉")
    print("=" * 60)
