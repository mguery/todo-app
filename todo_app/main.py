from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True: 
    user_action = input("type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] 
        
        todos = get_todos()
        
        todos.append(todo.capitalize() + '\n')         
        
        write_todos(todos) 

    elif user_action.startswith('show'):
        todos = get_todos()
        
        for index, item in enumerate(todos):
            item = item.strip('\n') 
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:].strip())
            print(number)
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError: 
            print("Your command is not valid")
            continue
            

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_done = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo '{todo_done}' was removed."
            print(message)
        except IndexError:
            print("There is no item with that number. Try again.")
            continue


    elif user_action.startswith('exit'):
        break
    
    else:
        print("Command is not valid")