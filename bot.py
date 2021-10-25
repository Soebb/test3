from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import os, datetime
import io
from PIL import Image
import mutagen
from mutagen.mp3 import MP3
import requests
from music_tag import load_file
from pyrogram.errors import FloodWait
import cv2

BOT_TOKEN = os.environ["BOT_TOKEN"]
Bot = Client(
    "Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


START_TXT = """
Hi {}, I'm test bot
"""

START_BTN = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Source Code', url='https://github.com/samadii/ChannelForwardTagRemover'),
        ]]
    )


@Bot.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TXT.format(update.from_user.mention)
    reply_markup = START_BTN
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )


@Bot.on_message(filters.video)
async def tag(bot, m):
    await m.download("vid.mp4")
    data = cv2.VideoCapture("vid.mp4")
    frames = data.get(cv2.CAP_PROP_FRAME_COUNT) 

    fps = int(data.get(cv2.CAP_PROP_FPS)) 

    seconds = int(frames / fps) 

    video_time = str(datetime.timedelta(seconds=seconds)) 

    print("duration in seconds:", seconds) 

    print("video time:", video_time) 


Bot.run()
