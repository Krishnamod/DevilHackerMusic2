import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_USERNAME
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/e770c634d5926d9d6319f.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 𝙃𝙚𝙡𝙡𝙤, 𝙄 𝘼𝙢 𝙎𝙪𝙥𝙚𝙧 𝙁𝙖𝙨𝙩 𝙈𝙪𝙨𝙞𝙘 𝙋𝙡𝙖𝙮𝙚𝙧
𝘽𝙤𝙩 𝙁𝙤𝙧 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝙂𝙧𝙤𝙪𝙥𝙨 ... 𝐃𝐞𝐩𝐥𝐨𝐲 𝐛𝐲 [𝐂𝐀𝐃𝐄𝐍](https://t.me/Caden_OP) 
┏━━━━━━━━━━━━━━━━━┓
┣★ 𝘾𝙧𝙚𝙖𝙩𝙤𝙧 : [𝐀𝐍𝐈𝐌𝐄](https://t.me/leva_anime_good)
┣★ 𝙎𝙪𝙥𝙥𝙤𝙧𝙩 : [𝐆𝐑𝐎𝐔𝐏](https://t.me/MUSIC_PLAYER_SUPPORT_CHAT)
┣★ 𝙎𝙊𝙐𝙍𝘾𝙀 : [𝗖𝗹𝗶𝗰𝗸 𝗛𝗲𝗿𝗲](https://t.me/vampire_baap)
┗━━━━━━━━━━━━━━━━━┛

━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "😆 ❰ 𝘼𝙙𝙙 𝙈𝙚 𝙄𝙣 𝙂𝙧𝙤𝙪𝙥 ❱ 😆", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "legend"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/e770c634d5926d9d6319f.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 𝙅𝙤𝙞𝙣 𝙃𝙚𝙧𝙚 𝘼𝙣𝙙 𝙎𝙪𝙥𝙥𝙤𝙧𝙩 💞", url=f"https://t.me/real_king_of_tg")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/8fddb775d567de8a63940.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "😆 𝘾𝙡𝙞𝙘𝙠 𝙃𝙚𝙧𝙚 𝙏𝙤 𝙂𝙚𝙩 𝙍𝙚𝙥𝙤 😆", url=f"https://t.me/real_king_of_tg")
                ]
            ]
        ),
    )
