# © @AnonymousBoy1025
import aiohttp
from pyrogram import filters

from FallenRobot import pbot
from FallenRobot.pyrogramee.errors import capture_err

__mod_name__ = "⛄𝐆𝐈𝐓𝐇𝐔𝐁☃️"

__help__ = """
I will give information about github profile 

 ❍ /github <username>*:* Get information about a GitHub user.
⏤͟͟͞͞•𓊈𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 ≛⃝🕊[@THE_VIP_BOY](https://t.me/the_vip_boy)⛦⃕͜🇮🇳𓊉
"""


@pbot.on_message(filters.command("github"))
@capture_err
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("/git username")
        return
    username = message.text.split(None, 1)[1]
    URL = f"https://api.github.com/users/{username}"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()
            try:
                url = result["html_url"]
                name = result["name"]
                company = result["company"]
                bio = result["bio"]
                created_at = result["created_at"]
                avatar_url = result["avatar_url"]
                blog = result["blog"]
                location = result["location"]
                repositories = result["public_repos"]
                followers = result["followers"]
                following = result["following"]
                caption = f"""**Info Of {name}**
**Username:** `{username}`
**Bio:** `{bio}`
**Profile Link:** [Here]({url})
**Company:** `{company}`
**Created On:** `{created_at}`
**Repositories:** `{repositories}`
**Blog:** `{blog}`
**Location:** `{location}`
**Followers:** `{followers}`
**Following:** `{following}`
⏤͟͟͞͞•𓊈𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 ≛⃝🕊[@THE_VIP_BOY](https://t.me/the_vip_boy)⛦⃕͜🇮🇳𓊉"""
            except Exception as e:
                print(str(e))
    await message.reply_photo(photo=avatar_url, caption=caption)
