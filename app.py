# start defining classes


class Employee:
    def __init__(self, id, name, tasks, role):
        self.id = id
        self.name = name
        self.tasks = tasks
        self.role = role

    def change_name(self, name):
        self.name = name

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)


class Task:
    def __init__(self, id, name, state):
        self.id = id
        self.name = name
        self.state = state

    def change_state(self, state):
        self.state = state


class State:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Role:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# end defining classes


# states
not_started = State(0, "not_started")
started = State(1, "started")
finished = State(2, "finished")

states = [not_started, started, finished]

# tasks

task0 = Task(0, "task0", not_started)
task1 = Task(1, "task1", not_started)
task2 = Task(2, "task2", not_started)

tasks = [task0, task1, task2]

# roles

admin = Role(0, "admin")
normale_employee = Role(1, "normale_employee")

roles = [admin, normale_employee]

# employees


employee0 = Employee(0, "employee0", [task0, task1], admin)
employee1 = Employee(1, "employee1", [task2], normale_employee)
employee2 = Employee(2, "employee2", [], normale_employee)


employees = [employee0, employee1, employee2]


for employee in employees:
    print("id: ", employee.id, ", name : ",
          employee.name + ", role : ", employee.role.name)
    print("**** tasks :")
    if (employee.tasks == []):
        print("no tasks")
    else:
        for task in employee.tasks:
            print(task.name)
    print("---")
