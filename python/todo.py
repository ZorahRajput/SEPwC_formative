import argparse
import os

TASK_FILE = "todo_list.txt"

            
def add_task(task):
    
        
    
def list_tasks():
    with open(TASK_FILE, "r") as file:
        tasks = file.readlines()
        counter = 1
        output_string = ""

        for i, task in enumerate(tasks): 
            if i == len(tasks) - 1: 
                output_string = output_string + str(counter) + ". " + task.strip() 
            else:
                output_string = output_string + str(counter) + ". " + task 
            counter = counter + 1
    return output_string
    file.close()
            

def remove_task(index):
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
