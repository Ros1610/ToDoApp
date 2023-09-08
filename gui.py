import PySimpleGUI as sg
import functions

todos = functions.read_file()

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do",
                         key="todo")
add_button = sg.Button("Add")
todos_list = sg.Listbox(values=todos, key="todos",
                        enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
delete_button = sg.Button("Delete")


window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button, edit_button], [todos_list, delete_button]],
                   font=('Helvetica', 11))

while True:
    event, value = window.read()
    print(event, value)
    match event:
        case "todos":
            window["todo"].update(value=value["todos"][0])

        case "Add":
            todos.append(value["todo"].strip().capitalize() + "\n")
            window["todos"].update(values=todos)
            window["todo"].update(value="")

        case "Edit":
            old_todo = value["todos"][0]
            number = todos.index(old_todo)
            new_todo = value["todo"].strip().capitalize() + "\n"
            todos[number] = new_todo
            window["todos"].update(values=todos)
            window["todo"].update(value="")

        case "Delete":
            num = todos.index(value["todos"][0])
            todos.pop(num)
            window["todos"].update(values=todos)
            window["todo"].update(value="")

        case sg.WIN_CLOSED:
            functions.write_file(todos)
            break

window.close()