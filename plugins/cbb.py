#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ 🖤 Mʏ ᴄʀᴇᴀᴛᴏʀ : <a href='https://t.me/RJ_Dubbers'>Rᴊ Dᴜʙʙᴇʀꜱ</a>\n○ 😺Dᴏɴᴀᴛᴇ ᴜꜱ ~ <a href='https://t.me/RJFilesBot?start=Z2V0LTIxMDQ1NDA1NzAxNDM5'>Cʟɪᴄᴋ Mᴇ</a>\n○ 🔥Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ 🥶sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ  : <a href='https://t.me/itz_sahil_official'>ᴘʀɪᴠᴀᴛᴇ ᴄᴏᴅᴇ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ᴄʟᴏsᴇ ᴍᴇ 🥀", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
