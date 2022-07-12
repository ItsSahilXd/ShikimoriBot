import nekos
import requests
from Shikimori import Application
from telegram.ext import CommandHandler
import random
import Shikimori.modules.waifu_string as waifu_string

url_sfw_1 = "https://api.waifu.pics/sfw/" 
url_sfw_2 = "https://nekos.best/"


def waifus(update, context):
    update.effective_message.reply_photo(random.choice(waifu_string.WAIFUS))

def swaifu(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}waifu" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_photo(photo=img)

def pout(update, context):
    msg = update.effective_message
    resp = requests.get("https://nekos.best/api/v2/pout")
    data = resp.json()
    img = (data["results"][0]["url"])
    msg.reply_animation(img)

def bored(update, context):
    msg = update.effective_message
    resp = requests.get("https://nekos.best/api/v2/bored")
    data = resp.json()
    img = (data["results"][0]["url"])
    msg.reply_animation(img)

def nekos2(update, context):
    msg = update.effective_message
    resp = requests.get("https://nekos.best/api/v2/neko")
    data = resp.json()
    img = (data["results"][0]["url"])
    msg.reply_photo(photo=img)

def stare(update, context):
    msg = update.effective_message
    resp = requests.get("https://nekos.best/api/v2/stare")
    data = resp.json()
    img = (data["results"][0]["url"])
    msg.reply_animation(img)

def think(update, context):
    msg = update.effective_message
    resp = requests.get("https://nekos.best/api/v2/think")
    data = resp.json()
    img = (data["results"][0]["url"])
    msg.reply_animation(img)

def thumbsup(update, context):
    msg = update.effective_message
    resp = requests.get("https://nekos.best/api/v2/thumbsup")
    data = resp.json()
    img = (data["results"][0]["url"])
    msg.reply_animation(img)

def waifu(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}waifu" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_photo(photo=img)

def neko(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}neko" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_photo(photo=img)

def shinobu(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}shinobu" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_photo(photo=img)

def megumin(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}megumin" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_photo(photo=img)

def bully(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}bully" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def cuddle(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}cuddle" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def cry(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}cry" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def hug(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}hug" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def awoo(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}awoo" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def kiss(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}kiss" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def lick(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}lick" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def pat(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}pat" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def smug(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}smug" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def bonk(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}bonk" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def yeet(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}yeet" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def blush(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}blush" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def smile(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}smile" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def wave(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}wave" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def highfive(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}highfive" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def handhold(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}handhold" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def nom(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}nom" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def bite(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}bite" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)


def glomp(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}glomp" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def slap(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}slap" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def killgif(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}kill" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def kickgif(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}kick" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def happy(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}happy" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def wink(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}wink" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def poke(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}poke" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def dance(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}dance" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def cringe(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}cringe" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

################
def wallpaper(update, context):
    msg = update.effective_message
    target = "wallpaper"
    msg.reply_photo(nekos.img(target))

def tickle(update, context):
    msg = update.effective_message
    target = "tickle"
    msg.reply_video(nekos.img(target))

def ngif(update, context):
    msg = update.effective_message
    target = "ngif"
    msg.reply_video(nekos.img(target))

def feed(update, context):
    msg = update.effective_message
    target = "feed"
    msg.reply_video(nekos.img(target))

def gasm(update, context):
    msg = update.effective_message
    target = "gasm"
    msg.reply_photo(nekos.img(target))

def avatar(update, context):
     msg = update.effective_message
     target = "avatar"
     msg.reply_photo(nekos.img(target))


def foxgirl(update, context):
    msg = update.effective_message
    target = "fox_girl"
    msg.reply_photo(nekos.img(target))

def gecg(update, context):
    msg = update.effective_message
    target = "gecg"
    msg.reply_photo(nekos.img(target))

def lizard(update, context):
    msg = update.effective_message
    target = "lizard"
    msg.reply_photo(nekos.img(target))
   
def goose(update, context):
    msg = update.effective_message
    target = "goose"
    msg.reply_photo(nekos.img(target))

def woof(update, context):
    msg = update.effective_message
    target = "woof"
    msg.reply_photo(nekos.img(target))   

def source(update, context):
    msg = update.effective_message
    img = "https://telegra.ph/file/f55d977a723b679197b43.mp4"
    msg.reply_animation(img)    

WALLPAPER_HANDLER = CommandHandler("wallpaper", wallpaper, block=False)
TICKLE_HANDLER = CommandHandler("tickle", tickle, block=False)
FEED_HANDLER = CommandHandler("feed", feed, block=False)
GASM_HANDLER = CommandHandler("gasm", gasm, block=False)
AVATAR_HANDLER = CommandHandler("avatar", avatar, block=False)
FOXGIRL_HANDLER = CommandHandler("foxgirl", foxgirl, block=False)
GECG_HANDLER = CommandHandler("gecg", gecg, block=False)
LIZARD_HANDLER = CommandHandler("lizard", lizard, block=False)
GOOSE_HANDLER = CommandHandler("goose", goose, block=False)
WOOF_HANDLER = CommandHandler("woof", woof, block=False)
NGIF_HANDLER = CommandHandler("ngif", ngif, block=False)

WAIFUS_HANDLER = CommandHandler("waifus", waifu, block=False)
NEKO_HANDLER = CommandHandler("neko", neko, block=False)
SHINOBU_HANDLER = CommandHandler("shinobu", shinobu, block=False)
MEGUMIN_HANDLER = CommandHandler("megumin", megumin, block=False)
BULLY_HANDLER = CommandHandler("bully", bully, block=False)
CUDDLE_HANDLER = CommandHandler("cuddle", foxgirl, block=False)
CRY_HANDLER = CommandHandler("cry", cry, block=False)
HUG_HANDLER = CommandHandler("hug", hug, block=False)
AWOO_HANDLER = CommandHandler("awoo", awoo, block=False)
KISS_HANDLER = CommandHandler("kiss", kiss, block=False)
LICK_HANDLER = CommandHandler("lick", lick, block=False)
PAT_HANDLER = CommandHandler("pat", pat, block=False)





SMUG_HANDLER = CommandHandler("smug", smug, block=False)
BONK_HANDLER = CommandHandler("bonk", bonk, block=False)
YEET_HANDLER = CommandHandler("yeet", yeet, block=False)
BLUSH_HANDLER = CommandHandler("blush", blush, block=False)
SMILE_HANDLER = CommandHandler("smile", smile, block=False)
WAVE_HANDLER = CommandHandler("wave", wave, block=False)
HIGHFIVE_HANDLER = CommandHandler("highfive", highfive, block=False)
HANDHOLD_HANDLER = CommandHandler("handhold", handhold, block=False)
NOM_HANDLER = CommandHandler("nom", nom, block=False)
BITE_HANDLER = CommandHandler("bite", bite, block=False)
GLOMP_HANDLER = CommandHandler("glomp", glomp, block=False)


SLAP_HANDLER = CommandHandler("slap", slap, block=False)
KILLGIF_HANDLER = CommandHandler("killgif", killgif, block=False)
HAPPY_HANDLER = CommandHandler("happy", happy, block=False)
WINK_HANDLER = CommandHandler("wink", wink, block=False)
POKE_HANDLER = CommandHandler("poke", poke, block=False)
DANCE_HANDLER = CommandHandler("dance", dance, block=False)
CRINGE_HANDLER = CommandHandler("cringe", cringe, block=False)

POUT_HANDLER = CommandHandler("pout", pout, block=False)
BORED_HANDLER = CommandHandler("bored", bored, block=False)
NEKOS_HANDLER = CommandHandler("nekos", nekos2, block=False)
STARE_HANDLER = CommandHandler("stare", stare, block=False)
THINK_HANDLER = CommandHandler("think", think, block=False)
THUMBSUP_HANDLER = CommandHandler("thumbsup", thumbsup, block=False)
WAIFU_HANDLER = CommandHandler('waifu', waifus, block=False)
Application.add_handler(WAIFU_HANDLER)
SWAIFU_HANDLER = CommandHandler('swaifu', swaifu, block=False)
Application.add_handler(SWAIFU_HANDLER)
SOURCE_HANDLER = CommandHandler('source', source, block=False)
Application.add_handler(SOURCE_HANDLER)
Application.add_handler(POUT_HANDLER)
Application.add_handler(BORED_HANDLER)
Application.add_handler(NEKOS_HANDLER)
Application.add_handler(STARE_HANDLER)
Application.add_handler(THINK_HANDLER)
Application.add_handler(THUMBSUP_HANDLER)

Application.add_handler(SLAP_HANDLER)
Application.add_handler(KILLGIF_HANDLER)
Application.add_handler(HAPPY_HANDLER)
Application.add_handler(WINK_HANDLER)
Application.add_handler(POKE_HANDLER)
Application.add_handler(DANCE_HANDLER)
Application.add_handler(CRINGE_HANDLER)


Application.add_handler(SMUG_HANDLER)
Application.add_handler(BONK_HANDLER)
Application.add_handler(YEET_HANDLER)
Application.add_handler(BLUSH_HANDLER)
Application.add_handler(SMILE_HANDLER)
Application.add_handler(WAVE_HANDLER)
Application.add_handler(HIGHFIVE_HANDLER)
Application.add_handler(HANDHOLD_HANDLER)
Application.add_handler(NOM_HANDLER)
Application.add_handler(BITE_HANDLER)
Application.add_handler(GLOMP_HANDLER)




Application.add_handler(AWOO_HANDLER)
Application.add_handler(PAT_HANDLER)
Application.add_handler(KISS_HANDLER)
Application.add_handler(LICK_HANDLER)
Application.add_handler(CRY_HANDLER)
Application.add_handler(HUG_HANDLER)
Application.add_handler(WAIFUS_HANDLER)
Application.add_handler(NEKO_HANDLER)
Application.add_handler(SHINOBU_HANDLER)
Application.add_handler(MEGUMIN_HANDLER)
Application.add_handler(BULLY_HANDLER)
Application.add_handler(CUDDLE_HANDLER)

Application.add_handler(LIZARD_HANDLER)
Application.add_handler(NGIF_HANDLER)
Application.add_handler(GOOSE_HANDLER)
Application.add_handler(WOOF_HANDLER)
Application.add_handler(GECG_HANDLER)
Application.add_handler(WALLPAPER_HANDLER)
Application.add_handler(TICKLE_HANDLER)
Application.add_handler(FEED_HANDLER)
Application.add_handler(GASM_HANDLER)
Application.add_handler(AVATAR_HANDLER)
Application.add_handler(FOXGIRL_HANDLER)

__handlers__ = [
    SLAP_HANDLER,
    LIZARD_HANDLER,
    GOOSE_HANDLER,
    WOOF_HANDLER,
    WALLPAPER_HANDLER,
    TICKLE_HANDLER,
    FEED_HANDLER,
    GASM_HANDLER,
    AVATAR_HANDLER,
    GECG_HANDLER,
    FOXGIRL_HANDLER,
    WAIFU_HANDLER,
]



__mod_name__ = "SFW"
__help__ = """
*Commands* *:*  
   ➢ `/neko`*:*Sends Random SFW Neko source Images.
   ➢ `/ngif`*:*Sends Random Neko GIFs.
   ➢ `/tickle`*:*Sends Random Tickle GIFs.
   ➢ `/feed`*:*Sends Random Feeding GIFs.
   ➢ `/gasm`*:*Sends Random Orgasm Stickers.
   ➢ `/avatar`*:*Sends Random Avatar Stickers.
   ➢ `/waifus`*:* Sends Random Waifu Stickers.
   ➢ `/waifu`*:* Sends Random Waifu image.
   ➢ `/swaifu`*:* Sends Random Waifu image.
   ➢ `/kiss`*:* Sends Random Kissing GIFs.
   ➢ `/cuddle`*:* Sends Random Cuddle GIFs.
   ➢ `/foxgirl`*:* Sends Random FoxGirl source Images.
   ➢ `/smug`*:* Sends Random Smug GIFs.
   ➢ `/gecg`*:* IDK
   ➢ `/slap`*:* Sends Random Slap GIFs.

*Some more SFW commands :*
   ➢ `/shinobu`
   ➢ `/megumin`
   ➢ `/bully`
   ➢ `/cry`
   ➢ `/awoo`
   ➢ `/lick`
   ➢ `/pat`
   ➢ `/bonk`
   ➢ `/yeet`
   ➢ `/blush`
   ➢ `/smile`
   ➢ `/wave`
   ➢ `/highfive`
   ➢ `/handhold`
   ➢ `/nom`
   ➢ `/bite`
   ➢ `/glomp`
   ➢ `/slapgif`
   ➢ `/kill`
   ➢ `/kick`
   ➢ `/happy`
   ➢ `/wink`
   ➢ `/poke`
   ➢ `/dance`
   ➢ `/cringe`
   ➢ `/pout`
   ➢ `/bored`
   ➢ `/nekos`
   ➢ `/stare`
   ➢ `/think`
   ➢ `/thumbsup`
   ➢ `/source`
"""

