from telethon import __version__, events, Button

from config import X1


START_BUTTON = [
    [
        Button.url("⌯ ᴧᴅᴅ ϻєєʜ ᴛσ ʏσυʀ ᴄʜᴧᴛ ⌯", "https://t.me/spmnvbot?startgroup=true")
    ],

    [
        Button.url("υᴘᴅᴧᴛєs ⎘", "https://t.me/axiombots"),
        Button.url("⌯ ᴧxɪσϻ ⌯", url="tg://user?id=7169279112")
    ],
    [
        Button.inline("⌯ ʜєʟᴘ ᴧηᴅ ᴄσϻϻᴧηᴅ ⌯", data="help_back")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
async def start(event):
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"""✦ ʜєʏ ʙᴧʙʏ <a href="tg://user?id={event.sender.id}">{event.sender.first_name}</a>, 📿

❖ ᴛʜɪs ɪs <a href="tg://user?id={bot_id}">{bot_name}</a>
➻ ᴧ ғᴧsᴛ & ᴘσᴡєʀғυʟ ᴛєʟєɢʀᴧϻ sᴘᴧϻ ʙσᴛ, ᴡɪᴛʜ sσϻє ᴧᴡєsσϻє ғєᴧᴛυʀєs.

•── ⋅ ⋅ ⋅ ──────── ⋅ • ⋅ ──────── ⋅ ⋅ ⋅ ──•
➤ ᴄʟɪᴄᴋ ση ᴛʜє ʜєʟᴘ ʙυᴛᴛση ᴛσ ɢєᴛ ɪηғσʀϻᴧᴛɪση ᴧʙσυᴛ ϻʏ ϻσᴅυʟєs ᴧηᴅ ᴄσϻϻᴧηᴅs.

➥ ϻʏ ᴅєᴠєʟσᴘєʀ : <a href="https://t.me/iii_maa7nav_iii/30">⌯ ϻᴧᴧηᴧᴠ ⌯</a>"""
        await event.client.send_file(
            event.chat_id,
            "https://files.catbox.moe/1yzzii.png",
            caption=TEXT,
            parse_mode="html",
            has_spoiler=True,
            buttons=START_BUTTON
        )
