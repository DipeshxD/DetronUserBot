import asyncio
import os
from datetime import datetime
from pathlib import Path
from telethon import events
from telethon import functions, types
from telethon.tl.types import InputMessagesFilterDocument
from mafiabot.utils import *
from userbot import *
from userbot import bot as mafiabot

DELETE_TIMEOUT = 5
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Mafia User"
mafia_logo = "https://telegra.ph/file/97747953cd5610d502f94.jpg"
h1m4n5hu0p = mafiabot.uid
mafia = f"[{DEFAULTUSER}](tg://user?id={h1m4n5hu0p})"

@mafiabot.on(admin_cmd(pattern=r"send (?P<shortname>\w+)", outgoing=True))
@mafiabot.on(sudo_cmd(pattern=r"send (?P<shortname>\w+)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    thumb = mafia_logo
    input_str = event.pattern_match.group(1)
    omk = f"**⍟ Plugin name ≈** `{input_str}`\n**⍟ Uploaded by ≈** {mafia}\n\n⚡ **[LEGENDARY AF DETRONBOT](https://t.me/DetronBot_Support)** ⚡"
    the_plugin_file = "./userbot/plugins/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
        lauda = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            thumb=thumb,
            caption=omk,
            force_document=True,
            allow_cache=False,
            reply_to=message_id,
        )
        await event.delete()
    else:
        await edit_or_reply(event, "File not found..... Kek")

@mafiabot.on(admin_cmd(pattern="install$", outgoing=True))
@mafia
