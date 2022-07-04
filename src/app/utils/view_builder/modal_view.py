class ModalView:
    def __init__(self, callback_id, title, submit, blocks):
        self.callback_id = callback_id
        self.title = title
        self.submit = submit if submit else "Submit"
        self.blocks = blocks

    def render(self):
        return self.__build_view();

    def __build_view(self):
        view = {
            "type": "modal",
            "callback_id": f"{self.callback_id}",
            "title": {"type": "plain_text", "text": f"{self.title}"},
            "submit": {"type": "plain_text", "text": f"{self.title}"},
        }

        blocks = []
        for element in self.blocks:
            blocks.append(element.build())
        view["blocks"] = blocks

        return view

