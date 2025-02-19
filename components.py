import json
import sys
from pathlib import Path

from datetime import datetime

BASE_DIR = Path(__file__).parent
TASK_DIR = BASE_DIR.joinpath("task.json")
TASK_DIR.touch()
cli_arguments = sys.argv[1:]


with open("task.json", encoding="utf8") as f:
    tasks = json.load(f)


def write_task(task_to_add):
    """
    Open and write in the json file
    :param task_to_add: task to add in the json file (dict)
    :return: None
    """

    with open("task.json", "w", encoding="utf8") as f:
        json.dump(task_to_add, f, indent=4, ensure_ascii=False)


def check_task_id_exist(t_id):
    return t_id in tasks


def modify_task_status(tks_id):

    if check_task_id_exist(tks_id):
        now = datetime.now()

        if cli_arguments[0] == "mark-done":
            t_status = "mark-done"
        else:
            t_status = "mark-in-progress"

        tasks[tks_id]["status"] = t_status
        tasks[tks_id]["updateAt"] = now.strftime("%Y %m %d %H:%M:%S")
        write_task(tasks)

    else:
        print("Task Id is not valide !")


def display_tasklist(status=""):
    """
    Displays all tasks or the tasks based on status
    :param status: task's status
    :return: None
    """
    todo_list = tasks.keys()
    if status:
        todo_list = list(filter((lambda x: tasks[x]["status"] == status), tasks))

    if todo_list:
        for i, task in enumerate(todo_list, start=1):
            print(f"Task {i}: {tasks[task]}")
    else:
        print("The tasklist is empty !")


def check_task_description_exist(description):
    desc = description.strip()

    for _, v in tasks.items():
        if v["description"] == desc:
            return False
    return True

