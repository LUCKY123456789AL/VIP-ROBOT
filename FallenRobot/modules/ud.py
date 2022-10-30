import requests
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async

from FallenRobot import dispatcher
from FallenRobot.modules.disable import DisableAbleCommandHandler


@run_async
def ud(update: Update, context: CallbackContext):
    message = update.effective_message
    text = message.text[len("/ud ") :]
    results = requests.get(
        f"https://api.urbandictionary.com/v0/define?term={text}"
    ).json()
    try:
        reply_text = f'*{text}*\n\n{results["list"][0]["definition"]}\n\n_{results["list"][0]["example"]}_'
    except:
        reply_text = "No results found."
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)


UD_HANDLER = DisableAbleCommandHandler(["ud"], ud)

dispatcher.add_handler(UD_HANDLER)

__help__ = """
» /ud (text) *:* Searchs the given text on Urban Dictionary and sends you the information.
⏤͟͟͞͞•𓊈𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 ≛⃝🕊[@THE_VIP_BOY](https://t.me/the_vip_boy)⛦⃕͜🇮🇳𓊉
"""
__mod_name__ = "🦜𝐔𝐑𝐁𝐀𝐍🦄"
__command_list__ = ["ud"]
__handlers__ = [UD_HANDLER]
