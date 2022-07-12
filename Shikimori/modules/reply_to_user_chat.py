# This module is made by https://github.com/SOME-1HING/
# You are free to use this module. But don't delete this commented text. Thank you.

from Shikimori import SHIKIMORI_PTB, MEDIA_BYE, MEDIA_GM, MEDIA_GN, MEDIA_HELLO
from telegram.constants import ParseMode
from telegram.ext import filters, MessageHandler
import time

IMG_GM = MEDIA_GM.split(".")
gm_id = IMG_GM[-1]

IMG_GN = MEDIA_GM.split(".")
gn_id = IMG_GN[-1]

IMG_HELLO = MEDIA_GM.split(".")
hello_id = IMG_HELLO[-1]

IMG_BYE = MEDIA_BYE.split(".")
bye_id = IMG_BYE[-1]

def goodnight(update, context):
    message = update.effective_message
    user1 = message.from_user.first_name
    try:
        if gn_id in ("jpeg", "jpg", "png"):
            update.effective_message.reply_photo(
            MEDIA_GN, caption = f"*Good Night:* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        elif gn_id in ("mp4", "mkv"):
            update.effective_message.reply_video(
            MEDIA_GN, caption = f"*Good Night:* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        elif gn_id in ("gif", "webp"):
            update.effective_message.reply_animation(
            MEDIA_GN, caption = f"*Good Night:* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        else:
            reply = f"*Good Night:* {user1}"
            message.reply_text(reply)

    except:
        reply = f"*Good Night:* {user1}"
        message.reply_text(reply)

    time.sleep(5)


def goodmorning(update, context):
    message = update.effective_message
    user1 = message.from_user.first_name
    try:
        if gm_id in ("jpeg", "jpg", "png"):
            update.effective_message.reply_photo(
            MEDIA_GM, caption = f"*Good Morning:* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        elif gm_id in ("mp4", "mkv"):
            update.effective_message.reply_video(
            MEDIA_GM, caption = f"*Good Morning:* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        elif gm_id in ("gif", "webp"):
            update.effective_message.reply_animation(
            MEDIA_GM, caption = f"*Good Morning:* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        else:
            reply = f"*Good Morning:* {user1}"
            message.reply_text(reply)
    except:
        reply = f"*Good Morning:* {user1}"
        message.reply_text(reply)
    
    time.sleep(5)

def hello(update, context):
    message = update.effective_message
    user1 = message.from_user.first_name
    try:
        if gm_id in ("jpeg", "jpg", "png"):
            update.effective_message.reply_photo(
            MEDIA_HELLO, caption = f"*Hello* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        elif gm_id in ("mp4", "mkv"):
            update.effective_message.reply_video(
            MEDIA_HELLO, caption = f"*Hello* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        elif gm_id in ("gif", "webp"):
            update.effective_message.reply_animation(
            MEDIA_HELLO, caption = f"*Hello* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        else:
            reply = f"*Hello* {user1}"
            message.reply_text(reply)
    except:
        reply = f"*Hello* {user1}"
        message.reply_text(reply)

    time.sleep(5)

def bye(update, context):
    message = update.effective_message
    user1 = message.from_user.first_name
    try:
        if bye_id in ("jpeg", "jpg", "png"):
            update.effective_message.reply_photo(
            MEDIA_BYE, caption = f"*Bye!!* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        elif bye_id in ("mp4", "mkv"):
            update.effective_message.reply_video(
            MEDIA_BYE, caption = f"*Bye!!* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        elif bye_id in ("gif", "webp"):
            update.effective_message.reply_animation(
            MEDIA_BYE, caption = f"*Bye!!* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
        else:
            reply = f"*Bye!!* {user1}"
            message.reply_text(reply)
    except:
        reply = f"*Bye!!* {user1}"
        message.reply_text(reply)
    
    time.sleep(5)



GDMORNING_HANDLER = MessageHandler(
    filters.Regex("(?i)(good morning|goodmorning)"), goodmorning, friendly="goodmorning", block=False
)
GDNIGHT_HANDLER = MessageHandler(
    filters.Regex("(?i)(good night|goodnight)"), goodnight, friendly="goodnight", block=False
)
BYE_HANDLER = MessageHandler(
    filters.Regex("(?i)(bye|brb|afk)"), bye, friendly="bye", block=False
)
HELLO_HANDLER = MessageHandler(
    filters.Regex("(?i)(hello)"), hello, friendly="hello", block=False
)

SHIKIMORI_PTB.add_handler(GDMORNING_HANDLER)
SHIKIMORI_PTB.add_handler(GDNIGHT_HANDLER)
SHIKIMORI_PTB.add_handler(HELLO_HANDLER)
SHIKIMORI_PTB.add_handler(BYE_HANDLER)