from functions import read_file, write_file, show_file
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)

todos = read_file()

while True:

    user_action = input("Type add, show, edit, complete, clear of exit: ").strip().lower()

    if user_action == 'add':
        todo = input("Enter a to-do: ").capitalize()
        todos.append(todo + "\n")

        print("The to-do has been added!")

    elif user_action.startswith("add"):
        todo = user_action[4:].capitalize()
        todos.append(todo + "\n")

        print("The to-do has been added!")

    elif user_action == 'show':
        show_file(todos)

    elif user_action == 'exit':
        print("Exiting the application...")
        break

    elif user_action == 'complete':
        show_file(todos)

        num = int(input("Enter the to-do number you have completed: ")) - 1
        todos.pop(num)

        print("The to-do has been removed from your list!")

    elif user_action.startswith('complete'):
        try:
            num = int(user_action[9:]) - 1
            todos.pop(num)

            print("The to-do has been removed from your list!")

        except ValueError:
            print("Enter the number of the to-do you have completed.")

        except IndexError:
            print("There is no to-do with such a number.")

    elif user_action == 'edit':
        show_file(todos)

        num = int(input("Enter the to-do number you want ot edit: ")) - 1
        todos[num] = input("Enter the edited to-do: ") + "\n"

        print("The to-do has been edited")

    elif user_action.startswith('edit'):
        try:
            num = int(user_action[5:]) - 1

            todos[num] = input("Enter the edited to-do: ") + "\n"

            print("The to-do has been edited!")

        except ValueError:
            print("Enter the number of the to-do you want to edit.")

        except IndexError:
            print("There is no to-do with such a number.")

    elif user_action == 'clear':
        todos.clear()

        print("The to-dos have been cleared!")

    else:
        print("Invalid input.")

write_file(todos)