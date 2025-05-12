from pyrogram import Client, filters
from database.mongo import set_sequence

@Client.on_message(filters.command("startseq"))
async def start_seq(client, message):
    set_sequence(message.from_user.id, True)
    await message.reply("Sequencing started. Send your files.")

@Client.on_message(filters.command("stopseq"))
async def stop_seq(client, message):
    set_sequence(message.from_user.id, False)
    await message.reply("Sequencing stopped.")
