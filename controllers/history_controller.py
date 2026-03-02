class HistoryController:
    def __init__(self, history_model):
        self.history_model = history_model

    def add_action(self, action):
        self.history_model.add_action(action)

    def get_history(self):
        return self.history_model.get_history()