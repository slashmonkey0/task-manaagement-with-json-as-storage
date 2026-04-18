import json
import os
from datetime import datetime

def input_task(name):
    task=[]
    with open("Tasks.json", "r") as file:
        data=json.load(file)
    for number in range(0,200):
        if number in data:
            continue
        else:
            break
    task.append(number)
    task.append(name)
    description= input("Enter task description: ")
    task.append(description)
    created_date=datetime.today().strftime("%Y-%m-%d")
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
        try:
            data=json.load(file)
        except json.JSONDecodeError:
            data = {}
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

def mark(id,status):
    with open("Tasks.json", "r") as file:
        data=json.load(file)
    #data[id][""]
    

while True:
    inputU= input("task_cli ")
    words= inputU.split()
    print(words)
    if words[0] == "add":
        add_task(words)
    elif words[0] == "list":
        list_tasks()
    elif words[0] == "mark":
        mark(words[1],words[2])
    elif words[0] == "exit":
        break
        
    
