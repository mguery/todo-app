def get_todos(filepath=r'C:\Users\msgue\OneDrive\Desktop\Marjy\Projects\Python\Python Mega Course\todo_app\files\todos.txt'):
    """
    Read text file and return list of to-dos
    """
    with open(filepath, 'r') as file_local:
            todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=r'C:\Users\msgue\OneDrive\Desktop\Marjy\Projects\Python\Python Mega Course\todo_app\files\todos.txt'):
    """
    Write to-dos in text file
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

