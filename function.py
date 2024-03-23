FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Read a text file and return the to-do list"""
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """write a to-do list in file (default: todos.txt)"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)