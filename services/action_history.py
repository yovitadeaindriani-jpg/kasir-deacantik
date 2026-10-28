class ActionHistory:
    def __init__(self):
        self.actions = []

    def push(self, action):
        self.actions.append(action)

    def pop(self):
        if not self.actions:
            return None
        return self.actions.pop()