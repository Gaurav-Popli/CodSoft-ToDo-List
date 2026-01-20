todo_list=[]


def add_new_task():
    task=input("Enter the task to add: \n")
    todo_list.append({"Task":task, "Status":"Pending"})
    print("Your new task has been added successfully\n")


def view_all_tasks():
    print("Your Tasks Are as Follows:\n")
    if len(todo_list)==0:
        print("You have No Pending Tasks\n")
    else:
        for index, task in enumerate(todo_list,1):
           print(f"{index}: {task['Task']}-{task['Status']}") 


def remove_task():
    try:
        if len(todo_list)==0:
            print("You Have No pending tasks\n")
        else:
            task_index=int(input("Enter the task number that you want to remove: \n"))-1

            if 0<=task_index<len(todo_list):
                remove_task=todo_list.pop(task_index)
                print(f"The Task '{remove_task}' has been removed successfully \n")
            else:
                print("Entered Invalid Task Number!!! Please Try Again!!!\n")
    except ValueError:
        print("Enter a valid Tasknumber!!!\n")


def mark_done():
    if len(todo_list)==0:
        print("you have no pending tasks!\n")
    else:
        try:
            task_index=int(input("Enter the task number to be marked as complete: \n"))-1
            if 0<=task_index<len(todo_list):
                todo_list[task_index]['Status']='completed'
                print(f"Task {todo_list[task_index]['Task']} has been marked as completed!!!\n")
            else:
                print("Invalid Task Number")
        except ValueError:
            print("Enter a Valid Task Number")


def menu():
    while(True):
        print("\n\nMAIN MENU")
        print("1.ADD A NEW TASK")
        print("2.VIEW ALL TASKS")
        print("3.REMOVE A TASK")
        print("4.MARK A TASK AS COMPLETED")
        print("5.EXIT")
        
        choice=int(input("ENTER A CHOICE FROM ABOVE MENU:" ))
        if(choice==1):
            add_new_task()
        elif choice==2:
            view_all_tasks()
        elif choice==3:
            remove_task()
        elif choice==4:
            mark_done()
        elif choice==5:
            print("Exiting the application...")
            exit()
        else:
            print("Invalid choice! Please Try Again!")

menu()

