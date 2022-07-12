from Shikimori import ALIVE_MEDIA, UPDATE_CHANNEL, SUPPORT_CHAT, OWNER_USERNAME, SHIKIMORI_PTB, NETWORK, NETWORK_USERNAME
from Shikimori.modules.disable import DisableAbleCommandHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

PHOTO = ALIVE_MEDIA

async def awake(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.effective_message
    buttons = [
        [
        InlineKeyboardButton(
            text="Updates",
            url=f"https://t.me/{UPDATE_CHANNEL}"),
        InlineKeyboardButton(
            text="Support",
            url=f"https://t.me/{SUPPORT_CHAT}"),
        ],
     ]
    
    first_name = update.effective_user.first_name
    user = message.from_user

    TEXT = f"""
    <b>Hi <a href="tg://user?id={user.id}">{first_name}</a>, I'm Shikomori Robot.

⚪ I'm Working Properly

⚪ My Owner : <a href="https://t.me/{OWNER_USERNAME}">{OWNER_USERNAME}</a></b>
    """
    if NETWORK:
        TEXT = TEXT + f'\n⚪ <b>I am Powered by : <a href="https://t.me/{NETWORK_USERNAME}">{NETWORK}</a>\n\n' + 'Thanks For Adding Me Here ❤️</b>'
    
    else:
        TEXT = TEXT + "\n<b>Thanks For Adding Me Here ❤️</b>"

    await message.reply_animation(PHOTO, caption=TEXT, reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.HTML)

SHIKIMORI_PTB.add_handler(DisableAbleCommandHandler("alive", awake))
__command_list__ = ["alive"]

__mod_name__ = "Alive ✨"
__help__ = """
*ALIVE*
 ❍ `/alive` :Check BOT status
"""
