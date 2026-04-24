# © @III_MAA7NAV_III
import asyncio

from random import choice

from telethon import events

from config import X1, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from AXIOMSPAM.data import HRAID, AXIOMM

HREPLY_RAID = []


@X1.on(events.NewMessage(incoming=True))
async def _(event):
    global HREPLY_RAID
    check = f"{event.sender_id}_{event.chat_id}"
    if check in HREPLY_RAID:
        await asyncio.sleep(0.1)
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(choice(HRAID)),
            reply_to=event.message.id,
        )


@X1.on(events.NewMessage(incoming=True, pattern=r"\%shrraid(?: |$)(.*)" % hl))
async def hrraid(e):
    if e.sender_id in SUDO_USERS:
        mkrr = e.text.split(" ", 1)
        if len(mkrr) == 2:
            entity = await e.client.get_entity(mkrr[1])

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)

        try:
            user_id = entity.id
            if user_id in AXIOMM:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴅᴇᴠᴇʟᴏᴘᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ")
            elif user_id == OWNER_ID:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ")
            elif user_id in SUDO_USERS:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ")
            else:
                global HREPLY_RAID
                check = f"{user_id}_{e.chat_id}"
                if check not in HREPLY_RAID:
                    HREPLY_RAID.append(check)
                await e.reply("⫸ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʜɪɴᴅɪ ʀᴇᴘʟʏʀᴀɪᴅ !! ✅")
        except NameError:
            await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐇𝐢𝐧𝐝𝐢 𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝\n ⫸  {hl}hrraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  ⫸ {hl}hrraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sdhraid(?: |$)(.*)" % hl))
async def dhraid(e):
    if e.sender_id in SUDO_USERS:
        text = e.text.split(" ", 1)

        if len(text) == 2:
            entity = await e.client.get_entity(text[1])
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)

        try:
            check = f"{entity.id}_{e.chat_id}"
            global HREPLY_RAID
            if check in HREPLY_RAID:
                HREPLY_RAID.remove(check)
            await e.reply("⫸ ʜɪɴᴅɪ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ !! ✅")
        except NameError:
            await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐃𝐇𝐢𝐧𝐝𝐢 𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝\n  ⫸ {hl}dhraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  ⫸ {hl}dhraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")



