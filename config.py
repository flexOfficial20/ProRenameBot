import re
import os
import time

id_pattern = re.compile(r'^.\d+$')


class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "24089031")  # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "0615e3afe13ddaaf8e9ddbd3977d35ff")  # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6914920593:AAFmSY16QTaaszWAdo0YQXm64Tq_2G0FXXo")  # ⚠️ Required

    # premium 4g renaming client
    STRING_API_ID = os.environ.get("STRING_API_ID", "6914920593")
    STRING_API_HASH = os.environ.get("STRING_API_HASH", "6914920593:AAFmSY16QTaaszWAdo0YQXm64Tq_2G0FXXo")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQFvkccAFLSR5WenJ4AKDD-Be1kafoLuxuULaCI19aLR2kDO0AuFXROab_OeTRd_b4BBh97i7SzEmqpSLe0ubDt-DHDq-lJCHWt4KMIgJrQmwRdKulYOZTb1uhQ-cUAaJgNyZSzVQRzTTSnzwa57gMSpIc2aYN5HObIxk9C5qor72133jNb7DzTSjYz-znJuc51EQiqfzh0KWcGeC5y5vLD45FR5e-vdbXHHeW1ogV32tnIWt9QIrr3f0zHd-NxYealn5tFSTsNWhi0dvH-AxDOVtyY1nz5teJG-oliReVBmA9Qhokr3tGYpGQ7UqWsHVPbBaFgJv4qxbFXeQZXNQxTLeccFXgAAAAGIe-pcAA")

    # database config
    DB_NAME = os.environ.get("DB_NAME", "Cluster0")
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://Mongo1:586637515hshhwfftqu@cluster0.tvy79ai.mongodb.net/?retryWrites=true&w=majority")  # ⚠️ Required

    # other configs
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/56d52ef4d9d395f6e72ca.jpg")
    ADMIN = [int(admin) if id_pattern.search(
        admin) else admin for admin in os.environ.get('ADMIN', "6584789596").split()]  # ⚠️ Required
    
    FORCE_SUB = os.environ.get("FORCE_SUB", "FleX_Bots_News") # ⚠️ Required Username without @
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002055707148"))  # ⚠️ Required
    FLOOD = int(os.environ.get("FLOOD", '10'))
    BANNED_USERS = set(int(x) for x in os.environ.get(
        "BANNED_USERS", "1234567890").split())

    # wes response configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


class Txt(object):
    # part of text configuration
    START_TXT = """<b>Hᴀɪ {} 👋,
Tʜɪs Is Aɴ Aᴅᴠᴀɴᴄᴇᴅ Aɴᴅ Yᴇᴛ Pᴏᴡᴇʀꜰᴜʟ Rᴇɴᴀᴍᴇ Bᴏᴛ
Usɪɴɢ Tʜɪs Bᴏᴛ Yᴏᴜ Cᴀɴ Rᴇɴᴀᴍᴇ & Cʜᴀɴɢᴇ Tʜᴜᴍʙɴᴀɪʟ Oꜰ Yᴏᴜʀ Fɪʟᴇ
Yᴏᴜ Cᴀɴ Aʟsᴏ Cᴏɴᴠᴇʀᴛ Vɪᴅᴇᴏ Tᴏ Fɪʟᴇ & Fɪʟᴇ Tᴏ Vɪᴅᴇᴏ
Tʜɪs Bᴏᴛ Aʟꜱᴏ Sᴜᴘᴘᴏʀᴛs Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Aɴᴅ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ</b>
"""

    ABOUT_TXT = """<b>╭───────────⍟
• ᴍy ɴᴀᴍᴇ : {}
• ᴘʀᴏɢʀᴀᴍᴇʀ : <a href=https://t.me/FLEXDUB_OFFICIAL>ғʟᴇx</a>
• ɴᴇᴛᴡᴏʀᴋ : <a href=https://t.me/emxes_network>ᴇᴍxᴇs</a> 
• ᴍᴏᴠɪᴇs : <a href=https://t.me/movieflix_original>ᴍᴏᴠɪᴇғʟɪx</a>
• sᴇʀɪᴇs : <a href=https://t.me/seriesflix_original>sᴇʀɪᴇsғʟɪx</a>
• ᴀɴɪᴍᴇ: <a href=https://t.me/ANIME_BARLOW>ᴀɴɪᴍᴇ ʙᴀʀʟᴏᴡ</a>
• ᴄʜᴀᴛ ɢʀᴏᴜᴘ: <a href=https://t.me/ANIME_IMMORTAL>ᴀɴɪᴍᴇ ᴄʜᴀᴛ ɢ</a>
• ᴍʏ ꜱᴇʀᴠᴇʀ : <a href=https://codeflix_bots>ᴠᴘs</a>
╰───────────────⍟ """

    HELP_TXT = """
🌌 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ</u></b>
  
<b>•></b> /start ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ sᴇɴᴅ ᴀɴʏ ᴘʜᴏᴛᴏ ᴛᴏ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ sᴇᴛ ᴛʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /del_thumb ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴏʟᴅ ᴛʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /view_thumb ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴛʜᴜᴍʙɴɪʟᴇ.


📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>

<b>•></b> /set_caption - <b>ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ sᴇᴛ ᴀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴩᴛɪᴏɴ</b>
<b>•></b> /see_caption - ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴩᴛɪᴏɴ
<b>•></b> /del_caption - ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴩᴛɪᴏɴ
<b>Exᴀᴍᴩʟᴇ:-</b> <code> /set_caption 📕 ғɪʟᴇ ɴᴀᴍᴇ: {filename}
💾 <b>sɪᴢᴇ:</b> {filesize}
⏰ <b>ᴅᴜʀᴀᴛɪᴏɴ:</b> {duration} </code>

✏️ <b><u>Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>
<b>•></b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nɴᴀᴍᴇ \nAɴᴅ Aᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ document, video, audio ].           


<b>➜ ᴘᴏᴡᴇʀᴇᴅ ʙʏ:</b> <a href=https://t.me/FleX_Bots_News>ғʟᴇX ʙᴏᴛs</a>
"""

    SEND_METADATA = """
❪ SET CUSTOM METADATA ❫

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Powered By:- @team_netflix" -metadata author="@Codeflix_bots" -metadata:s:s title="Subtitled By :- @Team_netflix" -metadata:s:a title="By :- @team_netflix" -metadata:s:v title="By:- @Codeflix_bots" </code>

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @Codeflix_bots
"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱➜
➜ 🗃️ sɪᴢᴇ: {1} | {2}
➜ ⏳️ ᴅᴏɴᴇ : {0}%
➜ 🚀 sᴘᴇᴇᴅ: {3}/s
➜ ⏰️ ᴇᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➜ </b>"""
