from Shikimori import SHIKIMORI_PTB
from Shikimori.modules.disable import DisableAbleCommandHandler

from Shikimori.modules.helper_funcs.alternate import send_message


def send(update, context):
	args = update.effective_message.text.split(None, 1)
	creply = args[1]
	send_message(update.effective_message, creply)
	
	
		

__help__ = """The Send Module Allows you to send a custom message to users in a chat
`/snd` :Send the given message
Note - /snd Hi will send the message hi to the chat"""

__mod_name__ = "Send"


ADD_CCHAT_HANDLER = DisableAbleCommandHandler("snd", send, block=False)
SHIKIMORI_PTB.add_handler(ADD_CCHAT_HANDLER)
__command_list__ = ["snd"]
__handlers__ = [
    ADD_CCHAT_HANDLER
]
