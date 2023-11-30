# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://telegra.ph/file/a5dde31d76a38bbe2b6b8.jpg",
    "https://telegra.ph/file/a5dde31d76a38bbe2b6b8.jpg",
    "https://telegra.ph/file/a5dde31d76a38bbe2b6b8.jpg",
    "https://telegra.ph/file/a5dde31d76a38bbe2b6b8.jpg",
    "https://telegra.ph/file/a5dde31d76a38bbe2b6b8.jpg",
    "https://telegra.ph/file/a5dde31d76a38bbe2b6b8.jpg",
    "https://telegra.ph/file/a5dde31d76a38bbe2b6b8.jpg",
]

HEY_IMG = "https://telegra.ph/file/a5dde31d76a38bbe2b6b8.jpg"

ALIVE_ANIMATION = [
    "https://telegra.ph//file/f9e2b9cdd9324fc39970a.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/c4c2759c5fc04cefd207a.mp4",
    "https://telegra.ph//file/b1fa6609b1c4807255927.mp4",
    "https://telegra.ph//file/f3c7147da6511fbe27c25.mp4",
    "https://telegra.ph//file/39071b73c02e3ff5945ca.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/6efdd8e28756bc2f6e53e.mp4",
]

BAN_GIFS = [
    "https://telegra.ph//file/85ac1ab12c833afa1a5dd.mp4",
]


KICK_GIFS = [
    "https://telegra.ph//file/79a6c527e6e6d530bcdc8.mp4",
]


MUTE_GIFS = [
    "https://telegra.ph//file/b4faf6e390d72d286abdf.mp4",
]

FIRST_PART_TEXT = "✨ *ʜᴇʟʟᴏ* `{}` . . ."

PM_START_TEXT = "✨ *ɪ ᴀᴍ ᴋɪʀɪᴛᴏ, ᴀ ɢᴇɴꜱʜɪɴ ɪᴍᴘᴀᴄᴛ ᴛʜᴇᴍᴇᴅ ʀᴏʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ʜᴜɢᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ*"

START_BTN = [
    [
        InlineKeyboardButton(
            text="Sᴜᴍᴍᴏɴ Mᴇ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="Cᴏᴍᴍᴀɴᴅs", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="Dᴇᴠ", url=f"tg://user?id={OWNER_ID}"),
        InlineKeyboardButton(text="Aɪ", callback_data="ai_handler"),
        InlineKeyboardButton(text="Uᴘᴅᴀᴛᴇs", url="https://t.me/AloneXBots"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="Sᴜᴍᴍᴏɴ Mᴇ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="Cʀᴇᴀᴛᴏʀ", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="Uᴘᴅᴀᴛᴇs", url="https://t.me/AloneXBots"),
        ib(text="Sᴜᴘᴘᴏʀᴛ", url="https://t.me/AlonesHeaven"),
    ],
    [
        ib(
            text="Sᴜᴍᴍᴏɴ Mᴇ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *ᴀʟᴏɴᴇ ʀᴏʙᴏᴛ* 🫧

☉ *Hᴇʀᴇ, Yᴏᴜ Will Fɪɴᴅ A Lɪsᴛ Oғ Aʟʟ Tʜᴇ Aᴠᴀɪʟʙʟᴇ Cᴏᴍᴍᴀɴᴅs.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
