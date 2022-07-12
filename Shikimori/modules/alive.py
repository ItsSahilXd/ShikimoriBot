from Shikimori import ALIVE_MEDIA, UPDATE_CHANNEL, SUPPORT_CHAT, OWNER_USERNAME, SHIKIMORI_PTB, NETWORK, NETWORK_USERNAME
from Shikimori.modules.disable import DisableAbleCommandHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from telegram.constants import ParseMode
from Shikimori.modules.helper_funcs.decorators import Shikimoricmd

PHOTO = ALIVE_MEDIA

@Shikimoricmd(command="alive")
async def awake(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    msg_id = update.effective_message.message_id
    bot = context.bot
    wallpaper = wallpaper.replace("\\", "")

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
    user = update.effective_user

    TEXT = f"""
    <b>Hi <a href="tg://user?id={user.id}">{first_name}</a>, I'm Shikomori Robot.

⚪ I'm Working Properly

⚪ My Owner : <a href="https://t.me/{OWNER_USERNAME}">{OWNER_USERNAME}</a></b>
    """
    if NETWORK:
        TEXT = TEXT + f'\n⚪ <b>I am Powered by : <a href="https://t.me/{NETWORK_USERNAME}">{NETWORK}</a>\n\n' + 'Thanks For Adding Me Here ❤️</b>'
    
    else:
        TEXT = TEXT + "\n<b>Thanks For Adding Me Here ❤️</b>"

    bot.send_photo(
        chat_id,
        photo=PHOTO,
        caption=TEXT,
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode=ParseMode.HTML,
        reply_to_message_id=msg_id,
    )

SHIKIMORI_PTB.add_handler(DisableAbleCommandHandler("alive", awake))
__command_list__ = ["alive"]

__mod_name__ = "Alive ✨"
__help__ = """
*ALIVE*
 ❍ `/alive` :Check BOT status
"""
