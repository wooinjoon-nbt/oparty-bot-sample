from abc import abstractmethod


class Action:
    def __init__(self, id):
        self.id = "action_" + id

    @abstractmethod
    def build(self):
        pass
