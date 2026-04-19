# task-manaagement-with-json-as-storage
A simple command-line based task manager built using Python and JSON for storage.  
This project allows you to create, update, delete, and manage tasks directly from the terminal.

---

## 🚀 Features

- Add new tasks
- List all tasks
- Filter tasks by status
- Update task descriptions
- Mark tasks as done/todo
- Delete tasks
- Persistent storage using JSON

---

## 📁 File Structure
- Tasks.json # Stores all tasks
- main.py # Your Python script
-  README.md

---

## ⚙️ How It Works

- Tasks are stored in `Tasks.json` as key-value pairs
- Each task has:
  - `description`
  - `Created_Date`
  - `updated_date`
  - `Status`

Example:
{
  "1": {
    "description": "do homework",
    "Created_Date": "24-04-19",
    "updated_date": "24-04-19",
    "Status": "todo"
  }
}
---
##Syntax
1)add
- Synatx: add description
---
Example: add do homework today

2) list
   - Synatx: list status
   ---
   -Examples:
   list todo
   list done
3) update
    - Synatx: update id new description
    ---
   Example:
   update 1 finish assignment
4) mark
    - Synatx: mark id status
   ---
   Examples:
   mark 1 done
   mark 2 todo
5) delete
    - Synatx: delete id
   ---
   Example:
   delete 1
