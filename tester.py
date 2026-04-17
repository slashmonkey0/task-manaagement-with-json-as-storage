import json
import os


def input_task(name):
    task=[]
    id= input("Enter task id: ")
    task.append(int(id))
    task.append(name)
    description= input("Enter task description: ")
    task.append(description)
    created_date= input("Enter task created date: ")
    task.append(created_date)
    task.append("not done")
    return task
    
def add_task(words):
    if os.path.exists("Tasks.json"):
        pass
    else:
        with open("Tasks.json", "w") as file:
            json.dump({}, file)

    task=input_task(words[1])
    with open("Tasks.json", "r") as file:
        data=json.load(file)
    data[task[0]] = {
        "name":task[1],
        "description":task[2],
        "Created_Date":task[3],
        "Status":task[4]
    }

    with open("Tasks.json", "w") as file:
        json.dump(data, file)

def list_tasks():
    file=open("Tasks.json","r")
    data=json.load(file)  
    for key, value in data.items():
        print(f"{key}: {value}")

while True:
    inputU= input("task_cli ")
    words= inputU.split()
    print(words)
    if words[0] == "add":
        add_task(words)
    elif words[0] == "list":
        list_tasks()
    elif words[0] == "exit":
        break
        
        
    
