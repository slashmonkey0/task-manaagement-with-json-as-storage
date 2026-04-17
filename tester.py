from asyncio import tasks
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
    return task
    
def add_task(words):
    if os.path.exists("Tasks.json"):
        pass
    else:
        with open("Tasks.json", "w") as file:
            json.dump([], file)
    task=input_task(words[1])
    file= open("Tasks.json", "r")
    data=json.load(file)
    data.append(task)
    file.close()
    file = open("Tasks.json", "w")
    json.dump(data, file)
    file.close()

def list_tasks():
    file=open("Tasks.json","r")
    data=json.load(file)
    for i in data:
        print(i)    

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
        
        
    
