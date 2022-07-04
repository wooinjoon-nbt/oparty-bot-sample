class SampleController:
    def message_hello(self, message, say):
        # say() sends a message to the channel where the event was triggered
        say(
            blocks=[
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": f"Hey there <@{message['user']}>!"},
                    "accessory": {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "Click Me"},
                        "action_id": "wow/button_click"
                    }
                }
            ],
            text=f"Hey there <@{message['user']}>!"
        )

    def action_button_click(self, body, ack, say, logger):
        # Acknowledge the action
        ack()
        say(f"<@{body['user']['id']}> clicked the button")
        logger.info(body)
