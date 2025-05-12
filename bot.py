from pyrogram import Client
import handlers.file_handler
import handlers.commands
from config import API_ID, API_HASH, BOT_TOKEN

app = Client("file_seq_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

app.run()
