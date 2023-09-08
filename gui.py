import PySimpleGUI as sg
import functions

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do",
                         key="todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 11))

todos = functions.read_file()

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos.append(values["todo"].strip().capitalize() + "\n")

        case sg.WIN_CLOSED:
            functions.write_file(todos)
            break


window.close()