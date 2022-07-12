# Module rewritten by https://github.com/SOME-1HING from the original module by rozari0

import requests
import random
import Shikimori.modules.animal_facts_string as animal_facts
from Shikimori import SHIKIMORI_PTB
from telegram import Update
from Shikimori.modules.disable import DisableAbleCommandHandler
from telegram.ext import ContextTypes


def animalfact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    update.effective_message.reply_text(random.choice(animal_facts.ANIMAL_FACTS))

def cats(update, context):
    msg = update.effective_message
    try:
        url = f'https://aws.random.cat/meow'
        result = requests.get(url).json()
        img = result['file']
        msg.reply_photo(photo=img)
    except:        
        url = f'https://aws.random.cat/meow'
        result = requests.get(url).json()
        img = result['file']
        msg.reply_photo(photo=img)

ANIMALFACT_HANDLER = DisableAbleCommandHandler("animalfacts", animalfact, block=False)
SHIKIMORI_PTB.add_handler(ANIMALFACT_HANDLER)
CAT_HANDLER = DisableAbleCommandHandler(("cats", "cat"), cats, block=False)
SHIKIMORI_PTB.add_handler(CAT_HANDLER)

__mod_name__ = "Animals"
__help__ = """
   ➢ `/animalfacts` - To Get random animal facts.
   ➢ `/cats` - To Get Random Photo of Cats.
   ➢ `/goose`*:* Sends Random Goose pic.
   ➢ `/woof`*:* Sends Random Woof pic.
   ➢ `/lizard`*:* Sends Random Lizard GIFs.
"""