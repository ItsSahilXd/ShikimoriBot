import os
import subprocess
import sys

from contextlib import suppress
from time import sleep

from Shikimori import SHIKIMORI_PTB
from Shikimori.modules.helper_funcs.chat_status import dev_plus
from telegram import Update
from telegram.error import Forbidden, TelegramError
from telegram.ext import ContextTypes, CommandHandler


@dev_plus
def leave(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bot = context.bot
    args = context.args
    if args:
        chat_id = str(args[0])
        try:
            bot.leave_chat(int(chat_id))
        except TelegramError:
            update.effective_message.reply_text(
                "Beep boop, I could not leave that group(dunno why tho).",
            )
            return
        with suppress(Forbidden):
            update.effective_message.reply_text("Beep boop, I left that soup!.")
    else:
        update.effective_message.reply_text("Send a valid chat ID")


@dev_plus
def gitpull(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sent_msg = update.effective_message.reply_text(
        "Pulling all changes from remote and then attempting to restart.",
    )
    subprocess.Popen("git pull", stdout=subprocess.PIPE, shell=True)

    sent_msg_text = sent_msg.text + "\n\nChanges pulled...I guess.. Restarting in "

    for i in reversed(range(5)):
        sent_msg.edit_text(sent_msg_text + str(i + 1))
        sleep(1)

    sent_msg.edit_text("Restarted.")

    os.system("restart.bat")
    os.execv("start.bat", sys.argv)


@dev_plus
def restart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.effective_message.reply_text(
        "Starting a new instance and shutting down this one",
    )

    os.system("restart.bat")
    os.execv("start.bat", sys.argv)


LEAVE_HANDLER = CommandHandler("leave", leave, block=False)
GITPULL_HANDLER = CommandHandler("gitpull", gitpull, block=False)
RESTART_HANDLER = CommandHandler("reboot", restart, block=False)

SHIKIMORI_PTB.add_handler(LEAVE_HANDLER)
SHIKIMORI_PTB.add_handler(GITPULL_HANDLER)
SHIKIMORI_PTB.add_handler(RESTART_HANDLER)

__mod_name__ = "Dev Commands"

___help__ = """
Here is help for Dev Commands.

Note: Consult with other devs before performing any actions.

❂ `/leave` <chat id> - Bot leaves the group.

**Only for self hosted bots.**
❂ `/reboot` - To restart Bot.
❂ `/gitpull` - Pull changes from github and redeploys the bot.
"""


__handlers__ = [LEAVE_HANDLER, GITPULL_HANDLER, RESTART_HANDLER]
