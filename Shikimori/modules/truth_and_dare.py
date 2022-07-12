import random
import Shikimori.modules.truth_and_dare_string as truth_and_dare_string
from Shikimori import app_build
from telegram import Update
from Shikimori.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext

def truth(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))

def dare(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))

def wyr(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(truth_and_dare_string.WYR))


def tord(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TORD))


TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth, block=False)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare, block=False)
TORD_HANDLER = DisableAbleCommandHandler("tord", tord, block=False)
WYR_HANDLER = DisableAbleCommandHandler(("rather", "wyr"), wyr, block=False)


app_build.add_handler(TRUTH_HANDLER)
app_build.add_handler(TORD_HANDLER)
app_build.add_handler(WYR_HANDLER)
app_build.add_handler(DARE_HANDLER)

__mod_name__ = "Truth or Dare"
__help__ = """
*Truth or Dare*
 ❍ `/truth` : Asks a question
 ❍ `/dare` : Tells a task to do
 ❍ `/tord` : Can either be a truth or dare
 ❍ `/rather` or `/wyr`: Would you rather?
"""
