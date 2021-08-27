from pyrogram import Client, filters
from pyrogram.errors import FloodWait


@Client.on_message(filters.channel & filters.edited & (filters.video | filters.document))
async def autopost(bot, update):
    media = update.video or update.document
    if (update.chat.id == -1001457054266):
        try:
            if "Ghermez" in media.file_name:
                await update.copy(chat_id=-1001166919373)
            elif "Chukurova" in media.file_name:
                await update.copy(chat_id=-1001437520825)
            elif "Mojeze" in media.file_name:
                await update.copy(chat_id=-1001071120514)
            elif "Yek Jonun Yek Eshgh" in media.file_name:
                await update.copy(chat_id=-1001546442991)
            elif "2020" in media.file_name:
                await update.copy(chat_id=-1001322014891)
            elif "Eshghe Mashroot" in media.file_name:
                await update.copy(chat_id=-1001409508844)
        except Exception as error:
            print(error)
