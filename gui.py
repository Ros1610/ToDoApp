import PySimpleGUI as sg
import functions
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

todos = functions.read_file()

label_todo = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do",
                         key="todo")
add_button = sg.Button("Add")
todos_list = sg.Listbox(values=todos, key="todos",
                        enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
delete_button = sg.Button("Delete")
exit_button = sg.Button("Save & Exit")

left_col_cont = [[label_todo],[input_box],[todos_list]]
right_col_cont = [[add_button],[edit_button],[delete_button],[exit_button]]
left_column = sg.Column(left_col_cont)
right_column = sg.Column(right_col_cont)

window = sg.Window("My To-Do App",
                   layout=[[left_column, right_column]],
                   font=("Helvetica", 11))

while True:
    event, value = window.read()
    match event:
        case "todos":
            window["todo"].update(value=value["todos"][0])

        case "Add":
            if value["todo"] == "":
                sg.popup("Please enter a to-do first.")
            else:
                todos.append(value["todo"].strip().capitalize() + "\n")
                window["todos"].update(values=todos)
                window["todo"].update(value="")

        case "Edit":
            try:
                old_todo = value["todos"][0]
                number = todos.index(old_todo)
                new_todo = value["todo"].strip().capitalize() + "\n"
                todos[number] = new_todo
                window["todos"].update(values=todos)
                window["todo"].update(value="")

            except IndexError:
                sg.popup("Please select a to-do.")

        case "Delete":
            try:
                todos.remove(value["todos"][0])
                window["todos"].update(values=todos)
                window["todo"].update(value="")

            except IndexError:
                sg.popup("Please select a to-do.")

        case "Save & Exit":
            functions.write_file(todos)
            break

        case sg.WIN_CLOSED:
            label_question = sg.Text("Do you want to save the changes?")
            yes_button = sg.Button("Yes")
            no_button = sg.Button("No")

            warning_window = sg.Window("Warning",
                                        layout=[[label_question], [yes_button, no_button]],
                                        font=("Helvetica", 11), modal=True)
            event = warning_window.read()
            match event[0]:
                case "Yes":
                    functions.write_file(todos)
                    break
                case "No":
                    break
                case sg.WIN_CLOSED:
                    break

window.close()