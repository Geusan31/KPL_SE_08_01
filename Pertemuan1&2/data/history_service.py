class HistoryService :
    def __init__(self):
        self.history = []

    def add_history(self, action):
        self.history.append(action)

    def get_history(self):
        return self.history