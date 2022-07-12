import requests
from Shikimori import SHIKIMORI_PTB
from Shikimori.modules.disable import DisableAbleCommandHandler
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import CallbackContext



def ud(update: Update, context: CallbackContext):
    message = update.effective_message
    args = context.args
    if len(args) == 0:
        return message.reply_text("/ud [word]")
        
    text = message.text[len('/ud '):]
    results = requests.get(
        f'https://api.urbandictionary.com/v0/define?term={text}').json()
    try:
        reply_text = f'*{text}*\n\n{results["list"][0]["definition"]}\n\n_{results["list"][0]["example"]}_'
    except:
        reply_text = "No results found."
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)


UD_HANDLER = DisableAbleCommandHandler(["ud"], ud, block=False)

SHIKIMORI_PTB.add_handler(UD_HANDLER)

__command_list__ = ["ud"]
__handlers__ = [UD_HANDLER]

__mod_name__ = "Urban Dictionary"
__help__ = """
*Urban Dictionary*
 ❍ `/ud` : Search for word in Urban Dictionary
"""
