class HistoryModel:
    def __init__(self, history_service):
        self.history_service = history_service

    def add_action(self, action):
        self.history_service.add_history(action)

    def get_history(self):
        return self.history_service.get_history()