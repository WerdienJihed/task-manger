class Task:
    def __init__(self, id, name, state):
        self.id = id
        self.name = name
        self.state = state

    def change_state(self, state):
        self.state = state
