import html
import random
import time

import Shikimori.modules.ExtraGifs_strings as ExtraGifs_strings
from Shikimori import SHIKIMORI_PTB
from Shikimori.modules.disable import DisableAbleCommandHandler
from Shikimori.modules.helper_funcs.chat_status import is_user_admin
from Shikimori.modules.helper_funcs.extraction import extract_user
from telegram import ChatPermissions, Update
from telegram.constants import ParseMode
from telegram.error import BadRequest
from telegram.ext import ContextTypes

GIF_ID = "CgACAgQAAx0CSVUvGgAC7KpfWxMrgGyQs-GUUJgt-TSO8cOIDgACaAgAAlZD0VHT3Zynpr5nGxsE"


def runs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.effective_message.reply_text(random.choice(ExtraGifs_strings.RUN_STRINGS))

def sanitize(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    name = (
        message.reply_to_message.from_user.first_name
        if message.reply_to_message
        else message.from_user.first_name
    )
    reply_animation = (
        message.reply_to_message.reply_animation
        if message.reply_to_message
        else message.reply_animation
    )
    reply_animation(random.choice(ExtraGifs_strings.GIFS), caption=f"*Sanitizes {name}*")


def slap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bot, args = context.bot, context.args
    message = update.effective_message
    chat = update.effective_chat

    reply_text = (
        message.reply_to_message.reply_text
        if message.reply_to_message
        else message.reply_text
    )

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id == bot.id:
        temp = random.choice(ExtraGifs_strings.SLAP_YONE_TEMPLATES)

        if isinstance(temp, list):
            if temp[2] == "tmute":
                if is_user_admin(chat, message.from_user.id):
                    reply_text(temp[1])
                    return

                mutetime = int(time.time() + 60)
                bot.restrict_chat_member(
                    chat.id,
                    message.from_user.id,
                    until_date=mutetime,
                    permissions=ChatPermissions(can_send_messages=False),
                )
            reply_text(temp[0])
        else:
            reply_text(temp)
        return

    if user_id:

        slapped_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(slapped_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    temp = random.choice(ExtraGifs_strings.SLAP_TEMPLATES)
    item = random.choice(ExtraGifs_strings.ITEMS)
    hit = random.choice(ExtraGifs_strings.HIT)
    throw = random.choice(ExtraGifs_strings.THROW)

    if update.effective_user.id == 1096215023:
        temp = "@NeoTheKitty scratches {user2}"

    reply = temp.format(user1=user1, user2=user2, item=item, hits=hit, throws=throw)

    reply_text(reply, parse_mode=ParseMode.HTML)

def pat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        patted_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(patted_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    pat_type = random.choice(("Text", "Gif", "Sticker"))
    if pat_type == "Gif":
        try:
            temp = random.choice(ExtraGifs_strings.PAT_GIFS)
            reply_to.reply_animation(temp)
        except BadRequest:
            pat_type = "Text"

    if pat_type == "Sticker":
        try:
            temp = random.choice(ExtraGifs_strings.PAT_STICKERS)
            reply_to.reply_sticker(temp)
        except BadRequest:
            pat_type = "Text"

    if pat_type == "Text":
        temp = random.choice(ExtraGifs_strings.PAT_TEMPLATES)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)


def roll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.reply_text(random.choice(range(1, 7)))

def shout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    text = " ".join(args)
    result = []
    result.append(" ".join(list(text)))
    for pos, symbol in enumerate(text[1:]):
        result.append(symbol + " " + "  " * pos + symbol)
    result = list("\n".join(result))
    result[0] = text[0]
    result = "".join(result)
    msg = "```\n" + result + "```"
    return update.effective_message.reply_text(msg, parse_mode="MARKDOWN")


def toss(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.reply_text(random.choice(ExtraGifs_strings.TOSS))



def shrug(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"¯\_(ツ)_/¯")



def bluetext(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "/BLUE /TEXT\n/MUST /CLICK\n/I /AM /A /STUPID /ANIMAL /THAT /IS /ATTRACTED /TO /COLORS"
    )


def rlg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    eyes = random.choice(ExtraGifs_strings.EYES)
    mouth = random.choice(ExtraGifs_strings.MOUTHS)
    ears = random.choice(ExtraGifs_strings.EARS)

    if len(eyes) == 2:
        repl = ears[0] + eyes[0] + mouth[0] + eyes[1] + ears[1]
    else:
        repl = ears[0] + eyes[0] + mouth[0] + eyes[0] + ears[1]
    update.message.reply_text(repl)


def decide(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_text = (
        update.effective_message.reply_to_message.reply_text
        if update.effective_message.reply_to_message
        else update.effective_message.reply_text
    )
    reply_text(random.choice(ExtraGifs_strings.DECIDE))

def eightball(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_text = (
        update.effective_message.reply_to_message.reply_text
        if update.effective_message.reply_to_message
        else update.effective_message.reply_text
    )
    reply_text(random.choice(ExtraGifs_strings.EIGHTBALL))


def table(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_text = (
        update.effective_message.reply_to_message.reply_text
        if update.effective_message.reply_to_message
        else update.effective_message.reply_text
    )
    reply_text(random.choice(ExtraGifs_strings.TABLE))


normiefont = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
weebyfont = [
    "卂",
    "乃",
    "匚",
    "刀",
    "乇",
    "下",
    "厶",
    "卄",
    "工",
    "丁",
    "长",
    "乚",
    "从",
    "𠘨",
    "口",
    "尸",
    "㔿",
    "尺",
    "丂",
    "丅",
    "凵",
    "リ",
    "山",
    "乂",
    "丫",
    "乙",
]

def weebify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/weebify <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)

SANITIZE_HANDLER = DisableAbleCommandHandler("sanitize", sanitize, block=False)
RUNS_HANDLER = DisableAbleCommandHandler("runs", runs, block=False)
SLAP_HANDLER = DisableAbleCommandHandler("slap", slap, block=False)
PAT_HANDLER = DisableAbleCommandHandler("pat", pat, block=False)
ROLL_HANDLER = DisableAbleCommandHandler("roll", roll, block=False)
TOSS_HANDLER = DisableAbleCommandHandler("toss", toss, block=False)
SHRUG_HANDLER = DisableAbleCommandHandler("shrug", shrug, block=False)
BLUETEXT_HANDLER = DisableAbleCommandHandler("bluetext", bluetext, block=False)
RLG_HANDLER = DisableAbleCommandHandler("rlg", rlg, block=False)
DECIDE_HANDLER = DisableAbleCommandHandler("decide", decide, block=False)
EIGHTBALL_HANDLER = DisableAbleCommandHandler("8ball", eightball, block=False)
TABLE_HANDLER = DisableAbleCommandHandler("table", table, block=False)
SHOUT_HANDLER = DisableAbleCommandHandler("shout", shout, block=False)
WEEBIFY_HANDLER = DisableAbleCommandHandler("weebify", weebify, block=False)

SHIKIMORI_PTB.add_handler(WEEBIFY_HANDLER)
SHIKIMORI_PTB.add_handler(SHOUT_HANDLER)
SHIKIMORI_PTB.add_handler(SANITIZE_HANDLER)
SHIKIMORI_PTB.add_handler(RUNS_HANDLER)
SHIKIMORI_PTB.add_handler(SLAP_HANDLER)
SHIKIMORI_PTB.add_handler(PAT_HANDLER)
SHIKIMORI_PTB.add_handler(ROLL_HANDLER)
SHIKIMORI_PTB.add_handler(TOSS_HANDLER)
SHIKIMORI_PTB.add_handler(SHRUG_HANDLER)
SHIKIMORI_PTB.add_handler(BLUETEXT_HANDLER)
SHIKIMORI_PTB.add_handler(RLG_HANDLER)
SHIKIMORI_PTB.add_handler(DECIDE_HANDLER)
SHIKIMORI_PTB.add_handler(EIGHTBALL_HANDLER)
SHIKIMORI_PTB.add_handler(TABLE_HANDLER)

__mod_name__ = "ᴍᴇᴍᴇs"
__command_list__ = [
    "runs",
    "slap",
    "roll",
    "toss",
    "shrug",
    "bluetext",
    "rlg",
    "decide",
    "table",
    "pat",
    "sanitize",
    "shout",
    "weebify",
    "8ball",
]
__handlers__ = [
    RUNS_HANDLER,
    SLAP_HANDLER,
    PAT_HANDLER,
    ROLL_HANDLER,
    TOSS_HANDLER,
    SHRUG_HANDLER,
    BLUETEXT_HANDLER,
    RLG_HANDLER,
    DECIDE_HANDLER,
    TABLE_HANDLER,
    SANITIZE_HANDLER,
    SHOUT_HANDLER,
    WEEBIFY_HANDLER,
    EIGHTBALL_HANDLER,
]
