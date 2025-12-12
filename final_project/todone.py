"""todone.py

Main application file for To Done CLI.
A productivity tool to manage tasks organized by focus areas.
"""

from task_manager import TaskManager


def show_help() -> None:
    """Display help information about using the application."""
    print("\n" + "=" * 60)
    print("HOW TO USE TO DONE")
    print("=" * 60)
    print("""
To Done helps you organize tasks by Focus Areas (like Work or
Personal life). Here's how it works:

1. SELECT A FOCUS AREA
   - Choose an existing focus area from the list (type number)
   - Create a new focus area if you need one (press A)
   - Edit focus area names to keep them organized (press S)
   - Delete focus areas you no longer need (press D)

2. MANAGE TASKS IN THAT AREA
   - Add new tasks with descriptions (press A)
   - View all tasks in the current focus area
   - Mark tasks complete when you finish them (press S)
   - Delete tasks you no longer need (press D)

3. KEYBOARD SHORTCUTS FOR FASTER USE
   - Type just a letter to select an option (e.g., "A" to add)
   - Or combine letter + number for quick actions:
     * "S1" or "S 1" = Complete task #1
     * "D2" or "D 2" = Delete task #2
   - This saves you time when managing multiple tasks!

4. SAVE YOUR WORK
   - Your tasks automatically save when you exit
   - Completed tasks are automatically cleaned up on exit
   - Your progress loads the next time you start the app

TIPS:
- Keep task descriptions clear and actionable
- Use focus areas to separate different parts of your life
- Limit focus areas to 2-7 for best results
- Complete tasks regularly to stay on track!
""")
    print("=" * 60)
    input("\nPress Enter to continue...")


def display_focus_area_menu(manager: TaskManager) -> None:
    """Display the focus area selection menu.

    Parameters
    ----------
    manager : TaskManager
        The task manager instance
    """
    print("\n" + "=" * 60)
    print("=== TO DONE: Focus on What Matters ===")
    print("=" * 60)
    print("\nYOUR FOCUS AREAS:")

    sorted_areas = sorted(manager.focus_areas)
    for i, area in enumerate(sorted_areas, 1):
        task_count = len(manager.get_tasks(area, include_completed=False))
        completed_count = len([t for t in manager.get_tasks(area) if t.is_complete])
        total_count = len(manager.get_tasks(area))
        print(f"  {i}. {area} ({task_count} active, {completed_count}/{total_count} complete)")

    print("\nOPTIONS:")
    print("  A. Create New Focus Area")
    print("  S. Edit Focus Area Name")
    print("  D. Delete Focus Area")
    print("  F. Help / How to Use")
    print("  G. Exit (Save & Quit)")
    
    # Show warning if approaching focus area limit
    if manager.at_focus_area_limit():
        remaining = manager.MAX_FOCUS_AREAS - len(manager.focus_areas)
        print(f"\n  ⚠️  Note: {remaining} focus area slots remaining (limit: {manager.MAX_FOCUS_AREAS})")
    
    print("=" * 60)


def select_focus_area(manager: TaskManager) -> str:
    """Handle focus area selection and management.

    Parameters
    ----------
    manager : TaskManager
        The task manager instance

    Returns
    -------
    str
        Selected focus area name, or empty string to exit
    """
    while True:
        display_focus_area_menu(manager)

        sorted_areas = sorted(manager.focus_areas)

        choice = input(f"\nSelect an option (1-{len(sorted_areas)} or A/S/D/F/G): ").strip().upper()

        if not choice:
            continue

        # Try to parse as number for focus area selection
        try:
            choice_num = int(choice)
            if 1 <= choice_num <= len(sorted_areas):
                return sorted_areas[choice_num - 1]
            else:
                print(f"\n✗ Please enter a number between 1 and {len(sorted_areas)}.")
                input("Press Enter to continue...")
                continue
        except ValueError:
            pass  # Not a number, check for letters

        # Create new focus area
        if choice == "A":
            new_area = input("\nEnter new focus area name: ").strip()
            if new_area:
                success, message = manager.add_focus_area(new_area)
                if success:
                    print(f"✓ {message}")
                else:
                    print(f"✗ {message}")
            else:
                print("✗ Focus area name cannot be empty.")
            input("Press Enter to continue...")

        # Edit focus area name
        elif choice == "S":
            if not sorted_areas:
                print("\n✗ No focus areas to edit. Create one first!")
                input("Press Enter to continue...")
                continue

            print("\nAVAILABLE FOCUS AREAS:")
            for i, area in enumerate(sorted_areas, 1):
                print(f"  {i}. {area}")

            area_choice = input(f"\nWhich focus area to rename? (1-{len(sorted_areas)}): ").strip()
            if not area_choice:
                continue

            try:
                area_num = int(area_choice)
                if 1 <= area_num <= len(sorted_areas):
                    old_name = sorted_areas[area_num - 1]
                    new_name = input(f"Enter new name for '{old_name}': ").strip()
                    if new_name:
                        if manager.rename_focus_area(old_name, new_name):
                            print(f"✓ Renamed '{old_name}' to '{new_name}'")
                        else:
                            print(f"✗ Could not rename. '{new_name}' may already exist.")
                    else:
                        print("✗ New name cannot be empty.")
                else:
                    print(f"✗ Please enter a number between 1 and {len(sorted_areas)}.")
            except ValueError:
                print("✗ Please enter a valid number.")
            input("Press Enter to continue...")

        # Delete focus area
        elif choice == "D":
            if not sorted_areas:
                print("\n✗ No focus areas to delete. Create one first!")
                input("Press Enter to continue...")
                continue

            print("\nAVAILABLE FOCUS AREAS:")
            for i, area in enumerate(sorted_areas, 1):
                task_count = len(manager.get_tasks(area))
                print(f"  {i}. {area} ({task_count} tasks)")

            area_choice = input(f"\nWhich focus area to delete? (1-{len(sorted_areas)}): ").strip()
            if not area_choice:
                continue

            try:
                area_num = int(area_choice)
                if 1 <= area_num <= len(sorted_areas):
                    area_to_delete = sorted_areas[area_num - 1]
                    task_count = len(manager.get_tasks(area_to_delete))
                    
                    if task_count > 0:
                        confirm = input(f"\n⚠️  This will delete '{area_to_delete}' and its {task_count} task(s). Continue? (y/N): ").strip().lower()
                        if confirm != 'y':
                            print("✗ Deletion cancelled.")
                            input("Press Enter to continue...")
                            continue
                    
                    deleted_tasks = manager.delete_focus_area(area_to_delete)
                    print(f"✓ Deleted '{area_to_delete}' and {deleted_tasks} task(s)")
                else:
                    print(f"✗ Please enter a number between 1 and {len(sorted_areas)}.")
            except ValueError:
                print("✗ Please enter a valid number.")
            input("Press Enter to continue...")

        # Help
        elif choice == "F":
            show_help()

        # Exit
        elif choice == "G":
            return ""

        else:
            print(f"\n✗ Invalid option. Please enter 1-{len(sorted_areas)} or A/S/D/F/G.")
            input("Press Enter to continue...")

        # Handle keyboard interrupt gracefully
        try:
            pass
        except (KeyboardInterrupt, EOFError):
            return ""


def display_task_menu(focus_area: str, tasks: list) -> None:
    """Display the task management menu with task list.

    Parameters
    ----------
    focus_area : str
        Current focus area name
    tasks : list
        List of tasks to display
    """
    print("\n" + "=" * 60)
    print(f"--- TASKS IN {focus_area.upper()} ---")
    
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks yet. Press A to add your first task!")
    
    print("\nOPTIONS:")
    print("  A. Add a New Task")
    print("  S. Complete a Task")
    print("  D. Delete a Task")
    print("  F. Back to Focus Areas")
    print("\nTIP: Type 'S1' to quickly complete task 1, or 'D2' to delete task 2")
    print("=" * 60)


def parse_task_command(command: str) -> tuple[str, int]:
    """Parse a command like 'S1' or 'D 2' into action and task number.

    Parameters
    ----------
    command : str
        The user's input command

    Returns
    -------
    tuple[str, int]
        (action_letter, task_number) or (action_letter, -1) if no number
    """
    command = command.strip().upper().replace(" ", "")
    
    if len(command) == 1:
        return command, -1
    
    if len(command) >= 2:
        action = command[0]
        try:
            task_num = int(command[1:])
            return action, task_num
        except ValueError:
            return command, -1
    
    return command, -1


def manage_tasks(manager: TaskManager, focus_area: str) -> None:
    """Handle task management for a specific focus area.

    Parameters
    ----------
    manager : TaskManager
        The task manager instance
    focus_area : str
        Current focus area name
    """
    while True:
        tasks = manager.get_tasks(focus_area, include_completed=True)
        display_task_menu(focus_area, tasks)

        command = input("\nEnter your choice (A/S/D/F or S1, D2, etc.): ").strip()
        
        if not command:
            continue
        
        action, task_num = parse_task_command(command)

        # Add new task
        if action == "A":
            title = input("\nEnter task description: ").strip()
            if title:
                manager.add_task(title, focus_area)
                print(f"✓ Task added to {focus_area}!")
            else:
                print("✗ Task description cannot be empty.")
            input("Press Enter to continue...")

        # Complete task
        elif action == "S":
            active_tasks = manager.get_tasks(focus_area, include_completed=False)
            if not active_tasks:
                print("\n✗ No active tasks to complete!")
                input("Press Enter to continue...")
                continue

            # If task number provided (e.g., S1), complete it immediately
            if task_num > 0:
                if 1 <= task_num <= len(active_tasks):
                    # Get index in full task list
                    all_tasks = manager.get_tasks(focus_area)
                    actual_index = all_tasks.index(active_tasks[task_num - 1])
                    if manager.complete_task(actual_index, focus_area):
                        print(f"✓ Task {task_num} marked as complete!")
                    else:
                        print("✗ Could not complete task.")
                else:
                    print(f"✗ Invalid task number. Choose 1-{len(active_tasks)}.")
                input("Press Enter to continue...")
                continue

            # Otherwise, prompt for task number
            print(f"\n--- ACTIVE TASKS IN {focus_area.upper()} ---")
            for i, task in enumerate(active_tasks, 1):
                print(f"{i}. {task}")

            try:
                task_input = input(f"\nWhich task to complete? (1-{len(active_tasks)}): ").strip()
                if task_input:
                    task_index = int(task_input) - 1
                    # Get index in full task list
                    all_tasks = manager.get_tasks(focus_area)
                    actual_index = all_tasks.index(active_tasks[task_index])
                    if manager.complete_task(actual_index, focus_area):
                        print(f"✓ Task marked as complete!")
                    else:
                        print("✗ Invalid task number.")
            except (ValueError, IndexError):
                print("✗ Invalid input.")
            input("Press Enter to continue...")

        # Delete task
        elif action == "D":
            if not tasks:
                print("\n✗ No tasks to delete!")
                input("Press Enter to continue...")
                continue

            # If task number provided (e.g., D2), confirm and delete
            if task_num > 0:
                if 1 <= task_num <= len(tasks):
                    task_to_delete = tasks[task_num - 1]
                    confirm = input(f"\n⚠️  Delete '{task_to_delete.title}'? (y/N): ").strip().lower()
                    if confirm == 'y':
                        if manager.delete_task(task_num - 1, focus_area):
                            print(f"✓ Task deleted!")
                        else:
                            print("✗ Could not delete task.")
                    else:
                        print("✗ Deletion cancelled.")
                else:
                    print(f"✗ Invalid task number. Choose 1-{len(tasks)}.")
                input("Press Enter to continue...")
                continue

            # Otherwise, show list and prompt
            print(f"\n--- TASKS IN {focus_area.upper()} ---")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

            try:
                task_input = input(f"\nWhich task to delete? (1-{len(tasks)}): ").strip()
                if task_input:
                    task_index = int(task_input) - 1
                    if 0 <= task_index < len(tasks):
                        task_to_delete = tasks[task_index]
                        confirm = input(f"\n⚠️  Delete '{task_to_delete.title}'? (y/N): ").strip().lower()
                        if confirm == 'y':
                            if manager.delete_task(task_index, focus_area):
                                print(f"✓ Task deleted!")
                            else:
                                print("✗ Could not delete task.")
                        else:
                            print("✗ Deletion cancelled.")
                    else:
                        print("✗ Invalid task number.")
            except ValueError:
                print("✗ Invalid input.")
            input("Press Enter to continue...")

        # Back to focus areas
        elif action == "F":
            break

        else:
            print("\n✗ Invalid option. Please enter A, S, D, or F (or S1, D2, etc.).")
            input("Press Enter to continue...")


def main():
    """Main application loop."""
    manager = TaskManager()

    try:
        while True:
            focus_area = select_focus_area(manager)

            if not focus_area:  # User chose to exit
                print("\n💾 Cleaning up and saving...")
                completed_count = manager.cleanup_completed_tasks()
                if completed_count > 0:
                    print(f"✓ Removed {completed_count} completed task(s)")
                manager.save_to_file()
                print("✓ All tasks saved successfully!")
                print("\n👋 Thanks for using To Done! Stay focused! 🎯\n")
                break

            # Manage tasks in selected focus area
            manage_tasks(manager, focus_area)

    except (KeyboardInterrupt, EOFError):
        print("\n\n💾 Cleaning up and saving...")
        completed_count = manager.cleanup_completed_tasks()
        if completed_count > 0:
            print(f"✓ Removed {completed_count} completed task(s)")
        manager.save_to_file()
        print("✓ All tasks saved successfully!")
        print("\n👋 Thanks for using To Done! Stay focused! 🎯\n")


if __name__ == "__main__":
    main()
