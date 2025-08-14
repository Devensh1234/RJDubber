#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7017755767:AAFbQLbXRGjuS6d_zDSZjisGzKnIWLbL2-Q")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "16575077"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1c8c0bcb55c14e0fd8078058966b6a11")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002162176259"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6264642175"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://NewPomPom:NewPomPom@cluster0.dyu5iru.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "pomoibot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001975852452"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b> Hᴇʟʟᴏ {first}🙌\n\nI ᴀᴍ Rᴊ ᴅᴜʙʙᴇʀ'ꜱ ꜰɪʟᴇ ʙᴏᴛ\nSᴜʙꜱᴄʀɪʙᴇ ᴛᴏ ᴍʏ Cʜᴀɴɴᴇʟ ᴛᴏ ɢᴇᴛ ​ᴇxᴄʟᴜꜱɪᴠᴇ Fɪʟᴇꜱ ☠️\n\nDᴜʙʙᴇᴅ Aɴɪᴍᴇꜱ ~ <a href='https://t.me/+JU06iz_ot-E4Zjc1'>Jᴏɪɴ Hᴇʀᴇ</a>\n\nDᴏɴᴀᴛᴇ ᴜꜱ ~ <a href='https://t.me/RJFilesBot?start=Z2V0LTIxMDQ1NDA1NzAxNDM5'>Click Me</a>\n\nPᴏᴡᴇʀᴇᴅ ʙʏ <a href='https://t.me/RJ_Dubbers'>Rᴊ Dᴜʙʙᴇʀꜱ🖤</a></b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join : <a href='https://t.me/RJDubber'>Cʟɪᴄᴋ Mᴇ 🖤</a></b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>Tʜᴀɴᴋ Yᴏᴜ ꜰᴏʀ ᴜꜱɪɴɢ Oᴜʀ ʙᴏᴛ..!\n\nPʟᴇᴀꜱᴇ Jᴏɪɴ - <a href='https://t.me/RJDUBBER'>Lᴀᴛᴇꜱᴛ Aɴɪᴍᴇ 🔥</a>\n\nTᴏ ɢᴇᴛ Aʟʟ ʟᴀᴛᴇꜱᴛ Aɴɪᴍᴇ🖤</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
