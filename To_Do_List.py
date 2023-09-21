# CLI Based To-do list application

# Add a Task

class Task:
    def __init__(self,title,description,task_id) -> None:
        self.title=title
        self.description=description
        self.task_id=task_id
        self.completed=False

tasks=[] 

def add_task():
    title= input("Enter title of task: ")
    description=input("Enter description of task: ")
    task_id= len(tasks)+1
    tasks.append(Task(title,description,task_id))
    print(f"Task {task_id} is added")


# List task

def list_task():
    for task in tasks:
        status="Complete" if task.completed else "Incomplete"
        print(f"Task ID: {task.task_id} Title: {task.title} Description: {task.description} Status: {status}")

# Mark as Complete

def mark_complete(task_id):
    for task in tasks:
        if task.task_id==task_id:
            task.completed=True
            print(f"Task {task_id} mark as complete")
            return
    print("Task not found")                 


# Mark as incomplete
def mark_not_complete(task_id):
    for task in tasks:
        if task.task_id==task_id:
            task.completed=False
            print(f"Task {task_id} mark as incomplete")
            return
    print("Task not found")        


# Delete as task
    
def delete_task(task_id):
    for task in tasks:
        if task.task_id==task_id:
            tasks.remove(task)
            print(f"Task {task_id} deleted")
            return
    print("Task not found")    


# Save task

def save_task(filename):
    with open(filename,"w") as file:
        for task in tasks:
            file.write(f"{task.task_id},{task.title},{task.description},{task.completed}\n")
    print("Task saved to file")


# Load Task
            
def load_task(filename):
    tasks.clear()
    try:
        with open(filename,"r") as file:
            for line in file:
                task_id,title,description,completed=line.strip().split(',')
                task=Task(title,description,int(task_id))     
                task.completed=(completed=="True")
                tasks.append(task) 
        print("Task loaded from files")
    except FileNotFoundError:
        print("No saved task found")


# User Friendly Interface

filename="task.txt"                          
load_task(filename)

while True:
    print("\n===== To-Do List Application =====")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Complete")
    print("4. Mark Task as Incomplete")
    print("5. Delete Task")
    print("6. Save Tasks")
    print("7. Quit")

    choice=input("Enter a choice: ")
    if choice=='1':
        add_task()
    elif choice=='2':
        list_task()
    elif choice=='3':
        task_id=int(input("Enter task to mark as complete: "))
        mark_complete(task_id)        
    elif choice=='4':    
        task_id=int(input("Enter task to mark as incomplete: "))
        mark_not_complete(task_id)
    elif choice=='5':
        task_id=int(input("Enter task to delete: "))    
        delete_task(task_id)
    elif choice=='6':
        save_task(filename)
    elif choice=='7':
        break
    else:
        print("Invalid Choice, Please Try again")

