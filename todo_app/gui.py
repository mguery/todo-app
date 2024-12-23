import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a task")
input_box = sg.InputText(tooltip="Enter to do", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My To Do App', 
                   layout=[[label], [input_box, add_button]],
                   font=('Arial', 16))

while True: 
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo']
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED: 
            break

window.close()