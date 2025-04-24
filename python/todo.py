"""
Created on Tue Apr 15 13:23:47 2025

@author: zorahrajput
"""
import argparse
import os

TASK_FILE = "todo_list.txt"
   
def add_task(task):
    """Appends a task to the end of the todo list file."""
    task="Item 6"
    try:
        with open(TASK_FILE, "a") as file:
            file.write(task + "\n")
        print(f"'{task}' has been added successfully to your list.")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def list_tasks():
    """Lists all tasks"""
    output_string = ""
    try:
        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()
            counter = 1

            if not tasks:
                return ""

            for i, task in enumerate(tasks):
                output_string += f"{counter}. {task.rstrip()}"
                if i < len(tasks) - 1:
                    output_string += "\n"
                counter += 1
        return output_string
    except FileNotFoundError:
        return ""
    except Exception as e:
        return ""

def remove_task(index_str):
    """Removes a task by index."""
    try:
        index = int(index_str) # converts the string to an integer
        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()

        if 1 <= index <= len(tasks):
            removed_task = tasks.pop(index - 1).strip() # index used as integer
            with open(TASK_FILE, "w") as file:
                file.writelines(tasks)
            print(f"Task '{removed_task}' (number {index}) has been removed.")
        elif tasks:
            print(f"Error: Task number {index} is not valid. Please enter a number between 1 and {len(tasks)}.")
        else:
            print("Error: The task list is empty, no tasks to remove.")

    except FileNotFoundError:
        print(f"Error: The file '{TASK_FILE}' was not found.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer for the task number.")
    except Exception as e:
        print(f"An error occurred while removing the task: {e}")

    
def main():
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    parser.add_argument("-a", "--add", help="Add a new task")
    parser.add_argument("-l", "--list", action="store_true", help="List all tasks")
    parser.add_argument("-r", "--remove", help="Remove a task by index")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        list_tasks()
    elif args.remove:
        remove_task(args.remove)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
