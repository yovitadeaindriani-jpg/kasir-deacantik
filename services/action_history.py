
class ActionHistory:
    def __init__(self):
        self.actions = []

    def push(self, action):
        self.actions.append(action)

    def undo(self):
        if self.actions:
            return self.actions.pop()
        return None

    def all(self):
        return self.actions.copy()
