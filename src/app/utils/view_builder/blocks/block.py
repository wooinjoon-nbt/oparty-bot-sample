from abc import abstractmethod


class Block:
    def __init__(self, id):
        self.id = "block_" + id

    @abstractmethod
    def build(self):
        pass
