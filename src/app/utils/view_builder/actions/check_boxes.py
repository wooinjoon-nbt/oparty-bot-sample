from src.app.utils.view_builder.actions.action import Action


class CheckBoxes(Action):
    def __init__(self, id, options):
        super().__init__(id)
        self.action_key = "accessory"
        self.type = "checkboxes"
        self.options = options

    def build(self):
        action_block = {
            "action_id": self.id,
            "type": self.type,
            "options": self.options
        }

        return self.action_key, action_block
