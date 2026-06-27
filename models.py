
from datetime import datetime


class Task:
    def __init__(self, title, description, deadline, priority,
                 status='pending'):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.priority = priority
        self.status = status

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "deadline": self.deadline,
            "priority": self.priority,
            "status": self.status
        }
    @classmethod
    def from_dict(cls, data):
        return cls(**data)

class Project:
    def __init__(self,name):
        self.name = name
        self.tasks = []

    def add_task(self,task):
        self.tasks.append(task)

    def remove_task(self,title):
        self.tasks = [task for task in self.tasks
                      if task.title != title]

    def to_dict(self):
        return {
            "name": self.name,
            "tasks": [task.to_dict() for task in self.tasks]
        }

    @classmethod
    def from_dict(cls, data):
        project = cls(data['name'])
        project.tasks = [Task.from_dict(task)
                         for task in data['tasks']]

        return project