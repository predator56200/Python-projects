"""
To-Do List
----------
A simple command-line to-do list that saves tasks to a text file,
so your list is still there the next time you run the program.

Concepts practiced: lists, menus, functions, reading and writing files
"""

import os

# Save tasks.txt in the same folder as this program, no matter where it is run from
FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.txt")


def load_tasks():
    """Read tasks from the file. Returns an empty list if the file doesn't exist yet."""
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def save_tasks(tasks):
    """Write every task to the file, one per line."""
    try:
        with open(FILENAME, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(task + "\n")
    except OSError as error:
        print(f"  Couldn't save your tasks: {error}")
        print("  Tip: unzip the folder first, then run the program from there.")


def show_tasks(tasks):
    if not tasks:
        print("  Your list is empty.")
        return
    for number, task in enumerate(tasks, start=1):
        print(f"  {number}. {task}")


def main():
    tasks = load_tasks()
    print("=== To-Do List ===")

    while True:
        print("\n1) View tasks  2) Add task  3) Complete task  4) Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            task = input("New task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print(f"  Added: {task}")

        elif choice == "3":
            show_tasks(tasks)
            if tasks:
                text = input("Number of the task you finished: ")
                if text.isdigit() and 1 <= int(text) <= len(tasks):
                    done = tasks.pop(int(text) - 1)
                    save_tasks(tasks)
                    print(f"  Nice work! Removed: {done}")
                else:
                    print("  That number isn't on the list.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("  Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        # Show any unexpected error instead of closing the window instantly
        print(f"\nSomething went wrong: {error}")
    # Keeps the window open when you double-click the file on Windows
    input("\nPress Enter to exit...")
