from telegram import Update
from telegram.ext import CallbackContext

from FallenRobot import dispatcher
from FallenRobot.modules.disable import DisableAbleCommandHandler

from TruthDarePy import TD

love = TD()


def truth(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_text(love.truth(lang="en"))


def dare(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_text(love.dare(lang="en"))


TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare)

dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)


__help__ = """
*Truth & Dare*

 ❍ /truth *:* Sends a random truth string.
 ❍ /dare *:* Sends a random dare string.
⏤͟͟͞͞•𓊈𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 ≛⃝🕊[@THE_VIP_BOY](https://t.me/the_vip_boy)⛦⃕͜🇮🇳𓊉
"""

__mod_name__ = "🍹𝐓𝐑𝐔𝐓𝐇🍸"
