
from models import Task,Project
from storage import save_data, load_data


projects = load_data()


def create_project():
    name =  input('Enter project name: ')
    projects.append(Project(name))

    save_data(projects)
    print("project created successfully")

def create_task():
    project_name = input('Enter project name: ')

    project = next(
        (p for p in projects if p.name == project_name))

    if not project:
        print('project not exist')
        return

    title = input('Enter title: ')
    description = input('Enter description: ')
    deadline = input('Enter deadline: ')
    priority = input('Enter priority: ')

    task = Task( title, description, deadline, priority)

    project.add_task(task)

    save_data(projects)

    print("task created successfully")


def view_tasks():
    if not projects:
        print('no project found')
        return

    for project in projects:
        print(f'project: {project.name} ')

        if not project.tasks:
            print('no tasks found')
            continue

        for task in project.tasks:
            print(
                f'\ntitle: {task.title} '
                f'\nstatus: {task.status}'
                f'\npriority: {task.priority}'
                f'\ndeadline: {task.deadline}'
            )


def change_status():
    project_name = input("Project name: ")

    project = next(
        (p for p in projects if p.name == project_name),
        None
    )

    if not project:
        print("Project not found.")
        return

    task_title = input("Task title: ")

    task = next(
        (t for t in project.tasks if t.title == task_title)
    )

    if not task:
        print("Task not found.")
        return

    print("1. pending")
    print("2. in-progress")
    print("3. completed")

    choice = input("Choose status: ")

    statuses = {
        "1": "pending",
        "2": "in-progress",
        "3": "completed"
    }

    if choice in statuses:
        task.status = statuses[choice]
        save_data(projects)
        print("Status updated.")
    else:
        print("Invalid choice.")


def delete_task():
    project_name = input("Project name: ")

    project = next(
        (p for p in projects if p.name == project_name),
        None
    )

    if not project:
        print("Project not found.")
        return

    task_title = input("Task title to delete: ")

    task = next(
        (t for t in project.tasks if t.title == task_title)
    )

    if not task:
        print("Task not found.")
        return

    project.tasks.remove(task)

    print("Task deleted successfully.")


def search_task():
    keyword = input("Enter task title: ").lower()

    found = False

    for project in projects:
        for task in project.tasks:
            if keyword in task.title.lower():
                print(
                    f"\nProject: {project.name}"
                    f"\nTitle: {task.title}"
                    f"\nDescription: {task.description}"
                    f"\nStatus: {task.status}"
                )
                found = True

    if not found:
        print("No matching task found.")