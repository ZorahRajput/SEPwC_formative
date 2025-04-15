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
    """Lists tasks within the task file"""
    with open(TASK_FILE, "r") as file:
        tasks = file.readlines()        
        counter = 1
        output_string = ""

        if not tasks:    
            print("Task list is empty") 
                
        for i, task in enumerate(tasks):
            if i == len(tasks) - 1: 
                output_string = output_string + str(counter) + ". " + task.strip() #removes new line function from final task in the list
            else:
                output_string = output_string + str(counter) + ". " + task 
            counter = counter + 1
            
    return output_string
                        

def remove_task():
    return 


def main():
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    parser.add_argument(
            "-a",
            "--add",
            help="Add a new task"
            )
    parser.add_argument(
            "-l",
            "--list",
            action="store_true",
            help="List all tasks")
    parser.add_argument(
            "-r",
            "--remove",
            help="Remove a task by index")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        tasks = list_tasks()
        print(tasks)
    elif args.remove:
        remove_task(int(args.remove))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
