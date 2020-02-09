from models.employee import Employee
from models.role import Role
from models.state import State
from models.task import Task


# functions

def display_all_employees():
    for employee in employees:
        print("id: ", employee.id, ", name : ",
              employee.name + ", role : ", employee.role.name)
        print("**** tasks :")
        if (employee.tasks == []):
            print("no tasks")
        else:
            for task in employee.tasks:
                print(task.name, ":", task.state.name)
        print("---")


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


employee0 = Employee(0, "employee0", [
                     task0, task1], admin, "employee0@gmail.com", "passwordemployee0",)
employee1 = Employee(1, "employee1", [
                     task2], normale_employee, "employee1@gmail.com", "passwordemployee1",)
employee2 = Employee(2, "employee2", [], normale_employee,
                     "employee2@gmail.com", "passwordemployee2")
employees = [employee0, employee1, employee2]


display_all_employees()

task3 = Task(3, "task3", not_started)

employee0.add_task(task3)

display_all_employees()
