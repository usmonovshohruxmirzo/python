todos = []

def add_todo(todo):
    todo = { "id": len(todos) + 1, "todo": todo }
    todos.append(todo)

def delete_todo(i):
    del todos[i]

def update_todo(i, value):
    todos[i]["todo"] = value

def delete_all_todos():
    todos.clear()

def display_todos():
    if len(todos) == 0:
        print("No any todos :(")
    else:
        print("All Todos:")
        print("-----------")
        for i in range(0, len(todos)):
            print(f"{todos[i]["id"]}) {todos[i]["todo"]}")
        print("-----------")