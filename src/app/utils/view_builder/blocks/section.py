from src.app.utils.view_builder.blocks.block import Block


class Section(Block):
    def __init__(self, id, text, action):
        super().__init__(id)
        self.text = text
        self.action = action

    def build(self):
        block = {
            "type": "section",
            "text": {"type": "mrkdwn", "text": self.text},
            "block_id": f"{self.id}",
        }
        action_key, action = self.action.build()
        block[action_key] = action

        return block
