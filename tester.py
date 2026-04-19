import json
import os
from datetime import datetime

def making_task(description):
    task=[]
    with open("Tasks.json", "r") as file:
        try:
            data=json.load(file)
        except json.JSONDecodeError:
            data = {}
    id_found=False

    for id in range(1,200):
        if str(id) in data:
            continue
        else:
            id_found=True
            break
    if not(id_found):
        print("No ids available")
        return None

    task.append(id)
    task.append(description)
    created_date=datetime.today().strftime("%y-%m-%d")
    updated_date=datetime.today().strftime("%y-%m-%d")
    task.append(created_date)
    task.append(updated_date)
    task.append("todo")
    return task
    
def add_task(words):
    if os.path.exists("Tasks.json"):
        pass
    else:
        with open("Tasks.json", "w") as file:
            json.dump({}, file)

    task=making_task(words[1])
    with open("Tasks.json", "r") as file:
        try:
            data=json.load(file)
        except json.JSONDecodeError:
            data = {}
    data[task[0]] = {
        "description":task[1],
        "Created_Date":task[2],
        "updated_date":task[3],
        "Status":task[4]
    }
    with open("Tasks.json", "w") as file:
        json.dump(data, file)

def list_tasks():
    file=open("Tasks.json","r")
    data=json.load(file)  
    for key, value in data.items():
        print(f"{key}: {value}")

def list_tasks_status(status):
    file=open("Tasks.json","r")
    data=json.load(file)  
    for key, value in data.items():
        if value["Status"]==status:
            print(f"{key}: {value}")
    
def list_tasks_todo():
    file=open("Tasks.json","r")
    data=json.load(file)  
    for key, value in data.items():
        if value["Status"]=="todo":
            print(f"{key}: {value}")
        
def mark_task(id,status):
    with open("Tasks.json", "r") as file:
        data=json.load(file)
    if str(id) in data:
        data[str(id)]["Status"]=status
        data[str(id)]["updated_date"]=datetime.today().strftime("%y-%m-%d")
    else:
        print("Task not found")
        return None
    with open("Tasks.json", "w") as file:
        json.dump(data,file)

def delete_task(id):
    with open("Tasks.json","r") as file:
        data= json.load(file)
    if str(id) in data:
        del data[str(id)]
    else:
        print("Task not found")
        return None
    with open("Tasks.json","w") as file:
        json.dump(data,file)

def update_task(id,description):
    with open("Tasks.json","r") as file:
        data=json.load(file)
    if str(id) in data:
        data[str(id)]["description"]=description
        data[str(id)]["updated_date"]=datetime.today().strftime("%y-%m-%d")
    else:
        print("Task not found")
        return None
    with open("Tasks.json","w") as file:
        json.dump(data,file)

while True:
    inputU= input("task_cli ")
    words= inputU.split()
    if words[0] == "add":
        add_task(words)
    elif words[0] == "list":
        if len(words)==1:
            list_tasks()
        else:
            list_tasks_status(words[1])
    elif words[0]=="delete":
        delete_task(words[1])
    elif words[0] == "mark":
        mark_task(words[1],words[2])
    elif words[0] == "update":
        update_task(words[1],words[2])
    elif words[0] == "exit":
        break
        
    
