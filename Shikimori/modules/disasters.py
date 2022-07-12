import html
import json
import os
from typing import Optional

from Shikimori import (
    DEV_USERS,
    OWNER_ID,
    DRAGONS,
    SUPPORT_CHAT,
    DEMONS,
    TIGERS,
    WOLVES,
    SHIKIMORI_PTB,
)
from Shikimori.modules.helper_funcs.chat_status import (
    dev_plus,
    sudo_plus,
    whitelist_plus,
)
from Shikimori.modules.helper_funcs.extraction import extract_user
from Shikimori.modules.log_channel import gloggable
from telegram import Update
from telegram.error import TelegramError
from telegram.constants import ParseMode
from telegram.ext import ContextTypes, CommandHandler
from telegram.helpers import mention_html

ELEVATED_USERS_FILE = os.path.join(os.getcwd(), "Shikimori/elevated_users.json")


def check_user_id(user_id: int, context: ContextTypes.DEFAULT_TYPE) -> Optional[str]:
    bot = context.bot
    if not user_id:
        reply = "That...is a chat! baka ka omae?"

    elif user_id == bot.id:
        reply = "This does not work that way."

    else:
        reply = None
    return reply


# This can serve as a deeplink example.
# disasters =
# """ Text here """

# do not async, not a handler
# def send_disasters(update):
#    update.effective_message.reply_text(
#        disasters, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)

### Deep link example ends



@dev_plus
@gloggable
def addsudo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)
    rt = ""

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in DRAGONS:
        message.reply_text("This member is already a Friend")
        return ""

    if user_id in DEMONS:
        rt += "Requested HA to promote a Servant to Friend."
        data["supports"].remove(user_id)
        DEMONS.remove(user_id)

    if user_id in WOLVES:
        rt += "Requested HA to promote a Slave to Friend."
        data["whitelists"].remove(user_id)
        WOLVES.remove(user_id)

    data["sudos"].append(user_id)
    DRAGONS.append(user_id)

    with open(ELEVATED_USERS_FILE, "w") as outfile:
        json.dump(data, outfile, indent=4)

    update.effective_message.reply_text(
        rt
        + "\nSuccessfully promoted {} to Friend!".format(
            user_member.first_name
        )
    )

    log_message = (
        f"#Friend\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
    )

    if chat.type != "private":
        log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

    return log_message



@sudo_plus
@gloggable
def addsupport(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)
    rt = ""

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in DRAGONS:
        rt += "Requested HA to demote this Friend to Servant"
        data["sudos"].remove(user_id)
        DRAGONS.remove(user_id)

    if user_id in DEMONS:
        message.reply_text("This user is already a Servant.")
        return ""

    if user_id in WOLVES:
        rt += "Requested HA to promote this Slave to Servant"
        data["whitelists"].remove(user_id)
        WOLVES.remove(user_id)

    data["supports"].append(user_id)
    DEMONS.append(user_id)

    with open(ELEVATED_USERS_FILE, "w") as outfile:
        json.dump(data, outfile, indent=4)

    update.effective_message.reply_text(
        rt + f"\n{user_member.first_name} is promoted to Servant!"
    )

    log_message = (
        f"#Servant\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
    )

    if chat.type != "private":
        log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

    return log_message



@sudo_plus
@gloggable
def addwhitelist(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)
    rt = ""

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in DRAGONS:
        rt += "This member is a Friend, Demoting to Slave."
        data["sudos"].remove(user_id)
        DRAGONS.remove(user_id)

    if user_id in DEMONS:
        rt += "This user is Servant, Demoting to Slave."
        data["supports"].remove(user_id)
        DEMONS.remove(user_id)

    if user_id in WOLVES:
        message.reply_text("This user is already a Slave.")
        return ""

    data["whitelists"].append(user_id)
    WOLVES.append(user_id)

    with open(ELEVATED_USERS_FILE, "w") as outfile:
        json.dump(data, outfile, indent=4)

    update.effective_message.reply_text(
        rt + f"\nSuccessfully promoted {user_member.first_name} to a Slave!"
    )

    log_message = (
        f"#Slave\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))} \n"
        f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
    )

    if chat.type != "private":
        log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

    return log_message



@sudo_plus
@gloggable
def addtiger(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)
    rt = ""

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in DRAGONS:
        rt += "This member is a Friend, Demoting to Peasant."
        data["sudos"].remove(user_id)
        DRAGONS.remove(user_id)

    if user_id in DEMONS:
        rt += "This user is a Servant, Demoting to Peasant."
        data["supports"].remove(user_id)
        DEMONS.remove(user_id)

    if user_id in WOLVES:
        rt += "This user is a Slave, promoting to Peasant."
        data["whitelists"].remove(user_id)
        WOLVES.remove(user_id)

    if user_id in TIGERS:
        message.reply_text("This user is already a Peasant.")
        return ""

    data["tigers"].append(user_id)
    TIGERS.append(user_id)

    with open(ELEVATED_USERS_FILE, "w") as outfile:
        json.dump(data, outfile, indent=4)

    update.effective_message.reply_text(
        rt + f"\nSuccessfully promoted {user_member.first_name} to a Peasant!"
    )

    log_message = (
        f"#Peasant\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))} \n"
        f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
    )

    if chat.type != "private":
        log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

    return log_message



@dev_plus
@gloggable
def removesudo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in DRAGONS:
        message.reply_text("Requested HA to demote this user to Civilian")
        DRAGONS.remove(user_id)
        data["sudos"].remove(user_id)

        with open(ELEVATED_USERS_FILE, "w") as outfile:
            json.dump(data, outfile, indent=4)

        log_message = (
            f"#UNFriend\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
        )

        if chat.type != "private":
            log_message = "<b>{}:</b>\n".format(html.escape(chat.title)) + log_message

        return log_message

    else:
        message.reply_text("This user is not a Friend!")
        return ""



@sudo_plus
@gloggable
def removesupport(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in DEMONS:
        message.reply_text("Requested HA to demote this user to Civilian")
        DEMONS.remove(user_id)
        data["supports"].remove(user_id)

        with open(ELEVATED_USERS_FILE, "w") as outfile:
            json.dump(data, outfile, indent=4)

        log_message = (
            f"#UNServant\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
        )

        if chat.type != "private":
            log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

        return log_message

    else:
        message.reply_text("This user is not a Servant!")
        return ""



@sudo_plus
@gloggable
def removewhitelist(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in WOLVES:
        message.reply_text("Demoting to normal user")
        WOLVES.remove(user_id)
        data["whitelists"].remove(user_id)

        with open(ELEVATED_USERS_FILE, "w") as outfile:
            json.dump(data, outfile, indent=4)

        log_message = (
            f"#UNSlave\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
        )

        if chat.type != "private":
            log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

        return log_message
    else:
        message.reply_text("This user is not a Slave!")
        return ""



@sudo_plus
@gloggable
def removetiger(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in TIGERS:
        message.reply_text("Demoting to normal user")
        TIGERS.remove(user_id)
        data["tigers"].remove(user_id)

        with open(ELEVATED_USERS_FILE, "w") as outfile:
            json.dump(data, outfile, indent=4)

        log_message = (
            f"#UNPeasant\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
        )

        if chat.type != "private":
            log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

        return log_message
    else:
        message.reply_text("This user is not a Peasant!")
        return ""



@whitelist_plus
def whitelistlist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply = "<b>Known Slaves:</b>\n"
    m = update.effective_message.reply_text(
        "<code>Gathering intel..</code>", parse_mode=ParseMode.HTML
    )
    bot = context.bot
    for each_user in WOLVES:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)

            reply += f"• {mention_html(user_id, html.escape(user.first_name))}\n"
        except TelegramError:
            pass
    m.edit_text(reply, parse_mode=ParseMode.HTML)



@whitelist_plus
def tigerlist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply = "<b>Known Peasants:</b>\n"
    m = update.effective_message.reply_text(
        "<code>Gathering intel..</code>", parse_mode=ParseMode.HTML
    )
    bot = context.bot
    for each_user in TIGERS:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)
            reply += f"• {mention_html(user_id, html.escape(user.first_name))}\n"
        except TelegramError:
            pass
    m.edit_text(reply, parse_mode=ParseMode.HTML)



@whitelist_plus
def supportlist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bot = context.bot
    m = update.effective_message.reply_text(
        "<code>Gathering intel..</code>", parse_mode=ParseMode.HTML
    )
    reply = "<b>Known Servants:</b>\n"
    for each_user in DEMONS:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)
            reply += f"• {mention_html(user_id, html.escape(user.first_name))}\n"
        except TelegramError:
            pass
    m.edit_text(reply, parse_mode=ParseMode.HTML)



@whitelist_plus
def sudolist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bot = context.bot
    m = update.effective_message.reply_text(
        "<code>Gathering intel..</code>", parse_mode=ParseMode.HTML
    )
    true_sudo = list(set(DRAGONS) - set(DEV_USERS))
    reply = "<b>Known Friends:</b>\n"
    for each_user in true_sudo:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)
            reply += f"• {mention_html(user_id, html.escape(user.first_name))}\n"
        except TelegramError:
            pass
    m.edit_text(reply, parse_mode=ParseMode.HTML)



@whitelist_plus
def devlist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bot = context.bot
    m = update.effective_message.reply_text(
        "<code>Gathering intel..</code>", parse_mode=ParseMode.HTML
    )
    true_dev = list(set(DEV_USERS) - {OWNER_ID})
    reply = "<b>Best Friends:</b>\n"
    for each_user in true_dev:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)
            reply += f"• {mention_html(user_id, html.escape(user.first_name))}\n"
        except TelegramError:
            pass
    m.edit_text(reply, parse_mode=ParseMode.HTML)


__help__ = f"""
*⚠️ Notice:*
Commands listed here only work for users with special access are mainly used for troubleshooting, debugging purposes.
Group admins/group owners do not need these commands. 

*List all special users:*
 ❍ `/dragons`*:* Lists all Dragon disasters
 ❍ `/demons`*:* Lists all Demon disasters
 ❍ `/tigers`*:* Lists all Tigers disasters
 ❍ `/wolves`*:* Lists all Wolf disasters
 ❍ `/devs`*:* Lists all Dev members
 ❍ `/adddragon`*:* Adds a user to Dragon
 ❍ `/adddemon`*:* Adds a user to Demon
 ❍ `/addtiger`*:* Adds a user to Tiger
 ❍ `/addwolf`*:* Adds a user to Wolf
 ❍ `Add dev doesnt exist, devs should know how to add themselves. AKA, why are you even dev if you don't have access to the bot vars.`

*Ping:*
 ❍ `/ping`*:* gets ping time of bot to telegram server
 ❍ `/pingall`*:* gets all listed ping times

*Broadcast: (Bot owner only)*
*Note:* This supports basic markdown
 ❍ `/broadcastall`*:* Broadcasts everywhere
 ❍ `/broadcastusers`*:* Broadcasts too all users
 ❍ `/broadcastgroups`*:* Broadcasts too all groups

*Groups Info:*
 ❍ `/groups`*:* List the groups with Name, ID, members count as a txt
 ❍ `/leave` <ID>*:* Leave the group, ID must have hyphen
 ❍ `/stats`*:* Shows overall bot stats
 ❍ `/getchats`*:* Gets a list of group names the user has been seen in. Bot owner only
 ❍ `/ginfo` username/link/ID*:* Pulls info panel for entire group

*Access control:* 
 ❍ `/ignore`*:* Blacklists a user from using the bot entirely
 ❍ `/lockdown `<off/on>*:* Toggles bot adding to groups
 ❍ `/notice`*:* Removes user from blacklist
 ❍ `/ignoredlist`*:* Lists ignored users

*Speedtest:*
 ❍ `/speedtest`*:* Runs a speedtest and gives you 2 options to choose from, text or image output

*Module loading:*
 ❍ `/listmodules`*:* Lists names of all modules
 ❍ `/load modulename`*:* Loads the said module to memory without restarting.
 ❍ `/unload modulename`*:* Loads the said module frommemory without restarting memory without restarting the bot 

*Remote commands:*
 ❍ `/rban`*:* user group*:* Remote ban
 ❍ `/runban`*:* user group*:* Remote un-ban
 ❍ `/rpunch`*:* user group*:* Remote punch
 ❍ `/rmute`*:* user group*:* Remote mute
 ❍ `/runmute`*:* user group*:* Remote un-mute

*Windows self hosted only:*
 ❍ `/reboot`*:* Restarts the bots service
 ❍ `/gitpull`*:* Pulls the repo and then restarts the bots service

*Chatbot:* 
 ❍ `/listaichats`*:* Lists the chats the chatmode is enabled in
 
*Debugging and Shell:* 
 ❍ `/debug` <on/off>*:* Logs commands to updates.txt
 ❍ `/logs`*:* Run this in support group to get logs in pm
 ❍ `/eval`*:* Self explanatory
 ❍ `/sh`*:* Runs shell command
 ❍ `/shell`*:* Runs shell command
 ❍ `/clearlocals`*:* As the name goes
 ❍ `/dbcleanup`*:* Removes deleted accs and groups from db
 ❍ `/py`*:* Runs python code
 
*Global Bans:*
 ❍ `/gban` <id> <reason>*:* Gbans the user, works by reply too
 ❍ `/ungban`*:* Ungbans the user, same usage as gban
 ❍ `/gbanlist`*:* Outputs a list of gbanned users

*Global Blue Text*
 ❍ `/gignoreblue`*:* <word>*:* Globally ignorea bluetext cleaning of saved word across lunaBot.
 ❍ `/ungignoreblue`*:* <word>*:* Remove said command from global cleaning list

*luna Core*
*Owner only*
 ❍ `/send`*:* <module name>*:* Send module
 ❍ `/install`*:* <reply to a .py>*:* Install module 

*Heroku Settings*
*Owner only*
 ❍ `/usage`*:* Check your heroku dyno hours remaining.
 ❍ `/see var` <var>*:* Get your existing varibles, use it only on your private group!
 ❍ `/set var` <newvar> <vavariable>*:* Add new variable or update existing value variable.
 ❍ `/del var` <var>*:* Delete existing variable.
 ❍ `/logs` Get heroku dyno logs.

`⚠️ Read from top`
Visit @{SUPPORT_CHAT} for more information.
"""

SUDO_HANDLER = CommandHandler(("addfriend", "addsudo", "adddragon"), addsudo, block=False)
SUPPORT_HANDLER = CommandHandler(("addsupport", "addservant", "adddemon"), addsupport, block=False)
TIGER_HANDLER = CommandHandler(("addpeasant", "addtiger"), addtiger, block=False)
WHITELIST_HANDLER = CommandHandler(("addwhitelist", "addslave", "addwolf"), addwhitelist, block=False)
UNSUDO_HANDLER = CommandHandler(("removesudo", "removefriend", "removedragon"), removesudo, block=False)
UNSUPPORT_HANDLER = CommandHandler(("removesupport", "removeservant", "removedemon"), removesupport, block=False)
UNTIGER_HANDLER = CommandHandler(("removepeasant", "removetiger"), removetiger, block=False)
UNWHITELIST_HANDLER = CommandHandler(("removewhitelist", "removeslave", "removewolf"), removewhitelist, block=False)

WHITELISTLIST_HANDLER = CommandHandler(["slavelist", "slaves", "wolves", "wolflist"], whitelistlist, block=False)
TIGERLIST_HANDLER = CommandHandler(["peasantlist", "peasants", "tigers", "tigerlist"], tigerlist, block=False)
SUPPORTLIST_HANDLER = CommandHandler(["servantlist", "servants", "demons", "demonlist"], supportlist, block=False)
SUDOLIST_HANDLER = CommandHandler(["friendlist", "friends", "sudos", "dragons", "sudolist", "dragonlist"], sudolist, block=False)
DEVLIST_HANDLER = CommandHandler(["devlist", "bestfriends", "devs"], devlist, block=False)

SHIKIMORI_PTB.add_handler(SUDO_HANDLER)
SHIKIMORI_PTB.add_handler(SUPPORT_HANDLER)
SHIKIMORI_PTB.add_handler(TIGER_HANDLER)
SHIKIMORI_PTB.add_handler(WHITELIST_HANDLER)
SHIKIMORI_PTB.add_handler(UNSUDO_HANDLER)
SHIKIMORI_PTB.add_handler(UNSUPPORT_HANDLER)
SHIKIMORI_PTB.add_handler(UNTIGER_HANDLER)
SHIKIMORI_PTB.add_handler(UNWHITELIST_HANDLER)

SHIKIMORI_PTB.add_handler(WHITELISTLIST_HANDLER)
SHIKIMORI_PTB.add_handler(TIGERLIST_HANDLER)
SHIKIMORI_PTB.add_handler(SUPPORTLIST_HANDLER)
SHIKIMORI_PTB.add_handler(SUDOLIST_HANDLER)
SHIKIMORI_PTB.add_handler(DEVLIST_HANDLER)

__mod_name__ = "ᴅᴇᴠ"
__handlers__ = [
    SUDO_HANDLER,
    SUPPORT_HANDLER,
    TIGER_HANDLER,
    WHITELIST_HANDLER,
    UNSUDO_HANDLER,
    UNSUPPORT_HANDLER,
    UNTIGER_HANDLER,
    UNWHITELIST_HANDLER,
    WHITELISTLIST_HANDLER,
    TIGERLIST_HANDLER,
    SUPPORTLIST_HANDLER,
    SUDOLIST_HANDLER,
    DEVLIST_HANDLER,
]
