from pyrogram import Client
import handlers.file_handler
import handlers.commands
from config import API_ID, API_HASH, BOT_TOKEN

app = Client("file_seq_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

app.run()

from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bot is running!'

def run_flask():
    app.run(host="0.0.0.0", port=8000)

threading.Thread(target=run_flask).start()
