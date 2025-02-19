"""
    Task tracker is a project used to track and manage your tasks.
    The application should run from the command line, accept user actions and inputs as arguments,
    and store the tasks in a JSON file.
"""
from datetime import datetime
from components import (write_task, check_task_id_exist, tasks, modify_task_status, cli_arguments, display_tasklist,
                        check_task_description_exist)


def main():
    if cli_arguments:
        match cli_arguments[0]:
            case "add":
                if len(cli_arguments) > 1 and cli_arguments[1].strip():
                    task_id = len(tasks) + 1
                    now = datetime.now()
                    tasks[task_id] = {
                        "id": task_id,
                        "description": cli_arguments[1].strip(),
                        "status": "todo",
                        "createdAt": now.strftime("%Y %m %d %H:%M:%S"),
                        "updateAt": now.strftime("%Y %m %d %H:%M:%S")
                    }
                    write_task(tasks)
                    print(f"Task added successfully (ID: {task_id})")
                else:
                    print("Task to add must not be empty !")

            case "update":
                if len(cli_arguments) > 2 and cli_arguments[2].strip():
                    if check_task_id_exist(cli_arguments[1]) and check_task_description_exist(cli_arguments[2]):
                        now = datetime.now()
                        task_key = cli_arguments[1]
                        tasks[task_key]["description"] = cli_arguments[2].strip()
                        tasks[task_key]["updateAt"] = now.strftime("%Y %m %d %H:%M:%S")
                        write_task(tasks)
                    else:
                        print("Id is not valide or task description is already exist!")

                else:
                    print("Task description and id must not be empty !")

            case "delete":
                if len(cli_arguments) > 1 and cli_arguments[1].strip():
                    if check_task_id_exist(cli_arguments[1]):
                        id_task_del = cli_arguments[1]
                        del tasks[id_task_del]
                        write_task(tasks)
                    else:
                        print("Task Id is not valide !")
                else:
                    print("Task Id must not be empty !")

            case "mark-done" | "mark-in-progress":
                if len(cli_arguments) > 1 and cli_arguments[1].strip():
                    modify_task_status(cli_arguments[1])
                else:
                    print("Task Id must not be empty !")

            case "list":
                if len(cli_arguments) > 1:
                    task_status = cli_arguments[1]
                    if task_status == "todo":
                        display_tasklist(task_status)

                    elif task_status == "done":
                        display_tasklist(task_status)

                    elif task_status == "in-progress":
                        display_tasklist(task_status)

                else:
                    display_tasklist()

            case _:
                print("Please enter an action(add, update, delete etc.)!")

    else:
        print("Action is required(add, update, delete etc.)! Try again...")


if __name__ == '__main__':
    main()
