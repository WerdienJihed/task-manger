class Employee:
    def __init__(self, id, name, tasks, role, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.tasks = tasks
        self.role = role

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def change_task_state(self, task_to_change, new_state):
        for task in self.tasks:
            if (task == task_to_change):
                task.state = new_state
