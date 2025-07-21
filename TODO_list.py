
tasks = []

def show_tasks(tasks):
    if not tasks:
        print("\033[94mTask list is empty.\033[0m")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"\t\033[35m{i}. {task}\033[0m")

print("\n\033[1;92m------TO-DO List app------\033[0m\n")
print("\n\033[1;92m------Add Task------\033[0m\n")

#add
while True:
    user = input("Enter Tasks or \033[1;91m'stop'\033[0m to exit: ").strip()
    
    if not user:
        print("\033[1;93mEmpty task not allowed!\033[0m")
        continue

    if user.lower() == "stop":
        print(f"\n\033[1;91mTasks cannot be added further.\033[0m\n")
        break

    add = user.title()
    tasks.append(add)


#Functions
while True:
    print("\n\033[1;92mType what you want to perform.\033[0m\n")
    print("\033[1;93m1. Remove task. \t2. Show task.\n3. Sort 'A to Z'. \t4. Reverse task.\033[0m")
    functions = input("\nEnter function's number or name (or \033[1;94m'q'\033[0m to exit): ")
    #Remove the specific task

    if functions.lower() in ["1", "remove"]:
        func_remove = input("\nEnter task's name to remove it: ").title()
        try:
            tasks.remove(func_remove)
            print(f"\n{func_remove.title()} removed from the tasks\n")
            show_tasks(tasks)

        except ValueError:
            print(f"\n\033[1;91mTask doesn't exist in the Tasks.\033[0m")
            show_tasks(tasks)
        print("\n\033[1;92mTasks Updated\033[0m\n")

    #Print the tasks

    elif functions.lower() in ["2", "show"]:
        print(f"\n\033[1;94mMy Tasks:\033[0m")
        if tasks == []:
            print("\033[1;94mTask is empty\033[0m")
        show_tasks(tasks)
        print("\n")

    #sorting

    elif functions.lower() in ["3", "sort"]:
        tasks.sort()
        print(f"\nTask have been sorted:")
        show_tasks(tasks)
        
    #Reverse the tasks

    elif functions.lower() in ["4", "reverse"]:
        tasks.sort(reverse=True)
        print("\n\033[1;34mTask in reverse:\033[0m")
        show_tasks(tasks)
        print("\nTask is reversed.")

    #clear tasks
    elif functions.lower() in ["5", "clear"]:
        tasks.clear()
        print("\n\033[1;91mAll tasks cleared.\033[0m")


    #Exit the code

    elif functions.lower() == "q":
        break
print("\n\033[91mFunction Closed.\033[0m\n")