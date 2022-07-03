from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
from dotenv import load_dotenv
from db import db_manager
import logging

from src.app import routes

logging.basicConfig(level=logging.INFO)


load_dotenv()
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]

app = App(token=SLACK_BOT_TOKEN)


if __name__ == "__main__":
    db_manager.init()
    routes.init(app)
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
