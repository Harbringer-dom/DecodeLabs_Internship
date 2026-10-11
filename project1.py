# A decodelab python programme to take input from the user, store it and display.

import json
import os


DB_FILE = "tasks.json"

def load_database():
    
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as file:
            return json.load(file)
    return []

def save_database(Tasks):

    with open(DB_FILE, 'w') as file:
        json.dump(Tasks, file, indent=4)

def add_task_logic(Tasks, task_string):

    task_id = len(Tasks) + 1
    new_row = {
        "id": task_id,
        "task": task_string
    }
    Tasks.append(new_row)


def render_display(Tasks):

    print("\n=== SYSTEM DATABASE ===")
    if not Tasks:
        print("No records found.")
    else:
        for index, row in enumerate(Tasks):
            print(f"Index [{index}] -> ID: {row['id']} | Task: {row['task']}")
    print("=======================\n")

def main():
    Tasks = load_database()
    
    while True:
        
        render_display(Tasks)
        
        
        user_input = input("Enter a task or (type 'Nil' to finish): ").strip()
        
        if user_input == "Nil":
            
            save_database(Tasks)
            print("Data serialized to disk. Process terminated.")
            break
        elif user_input:
        
            add_task_logic(Tasks, user_input)

if __name__ == "__main__":
    main()




