import json
from models import Project, Task

FILE_NAME = 'tasks.json'


def save_data(projects):
    data = [project.to_dict() for project in projects]

    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def load_data():
    try:
        project_lst=[]
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            data = json.load(f)

            for p in data:
                project = Project(p['name'])

                for t in p['tasks']:
                    task = Task(t['title'], t['description'], t['deadline'], t['priority'])
                    project.tasks.append(task)

                project_lst.append(project)


        return project_lst


    except FileNotFoundError:
        return []

    except json.decoder.JSONDecodeError:
        print('json file is corrupted')
        return []