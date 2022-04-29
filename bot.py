from pyrogram import Client
import os

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

APP_ID = int(os.environ.get("APP_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "renamer",
        bot_token=TG_BOT_TOKEN,
        api_id=AP_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app.run()
