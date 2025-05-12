from pyrogram import Client, filters
from database.mongo import is_active, increase_count
from config import DUMP_CHANNEL

@Client.on_message(filters.private & filters.document | filters.video | filters.audio | filters.photo)
async def handle_file(client, message):
    user_id = message.from_user.id
    if not is_active(user_id):
        return await message.reply("Use /startseq to begin sequencing.")

    count = increase_count(user_id)
    file = message.document or message.video or message.audio or message.photo
    filename = f"File_{count}"

    if message.document:
        ext = message.document.file_name.split('.')[-1]
        filename += f".{ext}"

    caption = f"**{filename}**\nUploaded by @{message.from_user.username or 'user'}"
    await message.copy(DUMP_CHANNEL, caption=caption)
    await message.reply(f"Saved as: `{filename}`")
