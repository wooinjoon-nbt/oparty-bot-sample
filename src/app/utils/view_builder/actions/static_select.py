from src.app.utils.view_builder.actions.action import Action


class StaticSelect(Action):
    def __init__(self, id, placeholder, options):
        super().__init__(id)
        self.action_key = "accessory"
        self.type = "static_select"
        self.placeholder = placeholder
        self.options = options

    def build(self):
        action_block = {
            "action_id": self.id,
            "type": f"{self.type}",
            "placeholder": {
                "type": "plain_text",
                "text": f"{self.placeholder}"
            },
            "options": self.options
        }

        return self.action_key, action_block
