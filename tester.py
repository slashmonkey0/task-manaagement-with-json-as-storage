import json
import os

if os.path.exists("Tasks.json"):
    pass
else:
    file=  open("Tasks.json", "w")
    file.close()

class task:
        def __init__(self,id, name, description, created_date):
            self.id = id
            self.name = name
            self.description = description
            self.created_date = created_date
            self.updated_date= "NULL"
        def input_task():
            id= input("Enter task id: ")
            name= input("Enter task name: ")
            description= input("Enter task description: ")
            created_date= input("Enter task created date: ")
            return task(id, name, description, created_date)
def add_task(words):
    if os.path.exists("Tasks.json"):
        pass
    else:
        file=  open("Tasks.json", "w")
        file.close()
    task= task.input_task()
    words.pop(0)
    str1=" ".join(words)
    file= open("Tasks.json", "r")
    try:
        data= json.load(file)
    except json.JSONDecodeError:
        data = []
    data.append(str1)
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
        
        
    
