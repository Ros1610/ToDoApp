FILEPATH = "todos.txt"


def read_file(filepath_arg=FILEPATH):
    """Read the text file and return the list of to-do items."""
    with open(filepath_arg) as file:
        todos_local = file.readlines()

    return todos_local


def write_file(todos_arg, filepath_arg = FILEPATH):
    """Save the to-do items list in the file."""
    with open(filepath_arg, 'w') as file:
        file.writelines(todos_arg)


def show_file(todos_arg):
    for index, entry in enumerate(todos_arg):
        print(f"{index + 1}. {entry.capitalize()}", end="")