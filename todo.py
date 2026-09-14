import os
import json

print("TO-DO LIST")


print("1. Add a task")
print("2. View tasks")
print("3. Delete a task")
print("4. Quit")
list_b = []
if os.path.exists("tasks.json"):
    with open("tasks.json", "r") as f:
        list_b = json.load(f)

while True:
   try:
    a = int(input("Choose: "))
   except ValueError:
        print("Please enter a valid number.")
        continue
    if a == 1:
        b = input("Add the task: ")
        list_b.append(b)
        print("Added.")
    elif a == 2:
        if list_b == []:
            print("No tasks.")
        else:    
            for i in range(len(list_b)):
                print(f"{i+1}. {list_b[i]}")
    elif a == 3:
        c = input("Delete the task: ")
        coun = list_b.count(c)
        if coun == 0:
            print("Not there in the task.")
            continue
        else:
            for i in range(coun):
                list_b.remove(c)
        print("Deleted.")
    elif a == 4:
        print("Goodbye.")
        break
