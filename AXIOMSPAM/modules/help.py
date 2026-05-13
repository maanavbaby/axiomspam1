# © @III_MAA7NAV_III
from telethon import events, Button

from config import X1, SUDO_USERS, CMD_HNDLR as hl


HELP_STRING = f"<b>📗 ᴅɪᴠє ɪηᴛσ ᴧʟʟ ᴄσϻϻᴧηᴅ ᴄᴧᴛєɢσʀɪєs ʙєʟσᴡ</b>\n\n✧ ɢєᴛ ɢυɪᴅᴧηᴄє - ᴧssɪsᴛᴧηᴄє ɪη συʀ <a href='https://t.me/manavkiduniya'>sυᴘᴘσʀᴛ ᴄʜᴧᴛ</a> — ɪ'ϻ ʜєʀє ғσʀ ʏσυ!"

HELP_BUTTON = [
    [
      Button.inline("sᴘᴧϻ", data="spam"),
      Button.inline("ʀᴧɪᴅ", data="raid")
    ],
    [
      Button.inline("ϻσʀє", data="moreaxiomcmd"),
      Button.inline("ηєᴡ ᴄσϻϻᴧηᴅ", data="maanav")
    ]
  ]


@X1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
        try:
          await event.client.send_file(event.chat_id,
              "https://files.catbox.moe/1yzzii.png",
              caption=HELP_STRING,
              spoiler=True,
              parse_mode="html",
              buttons=HELP_BUTTON
              )
        except Exception as e:
            await event.client.send_message(event.chat_id, f"<b>⫸ An Exception Occured!\n\n⫸ERROR: {str(e)}</b>", parse_mode="html")


moreaxiomcmd_msg = f"""
<b><u>⫸ єxᴛʀᴧ ᴄσϻϻᴧηᴅs:</u></b>

<b>υsєʀʙσᴛ: υsєʀʙσᴛ ᴄϻᴅs
✧ {hl}ᴘɪηɢ
✧ {hl}ʀєʙσσᴛ
✧ {hl}sυᴅσ &lt;ʀєᴘʟʏ ᴛσ υsєʀ&gt; --> ᴧxɪσϻ ᴄϻᴅ
✧ {hl}ʟσɢs --> ᴧxɪσϻ ᴄϻᴅ</b>

<b>єᴄʜσ: ᴛσ ᴧᴄᴛɪᴠє єᴄʜσ ση ᴧηʏ υsєʀ
✧ {hl}єᴄʜσ &lt;ʀєᴘʟʏ ᴛσ υsєʀ&gt;
✧ {hl}ʀϻєᴄʜσ &lt;ʀєᴘʟʏ ᴛσ υsєʀ&gt;</b>

<b>ʟєᴧᴠє: ᴛσ ʟєᴧᴠє ɢʀσυᴘ/ᴄʜᴧηηєʟ
✧ {hl}ʟєᴧᴠє &lt;ɢʀσυᴘ/ᴄʜᴧᴛ ɪᴅ&gt;
✧ {hl}ʟєᴧᴠє : ᴛʏᴘє ɪη ᴛʜє ɢʀσυᴘ ʙσᴛ ᴡɪʟʟ ᴧυᴛσ ʟєᴧᴠє ᴛʜᴧᴛ ɢʀσυᴘ</b>
"""


raid_msg = f"""
<u><b>⫸ ʀᴧɪᴅ ᴄσϻϻᴧηᴅs:</b></u>

<b>ʀᴧɪᴅ: ᴧᴄᴛɪᴠᴧᴛєs ʀᴧɪᴅ ση ᴧηʏ ɪηᴅɪᴠɪᴅυᴧʟ υsєʀ ғσʀ ɢɪᴠєη ʀᴧηɢє
✧ {hl}ʀᴧɪᴅ &lt;ᴄσυηᴛ&gt; &lt;υsєʀηᴧϻє&gt;
✧ {hl}ʀᴧɪᴅ &lt;ᴄσυηᴛ&gt; &lt;ʀєᴘʟʏ ᴛσ υsєʀ&gt;</b>

<b>ʀєᴘʟʏʀᴧɪᴅ: ᴧᴄᴛɪᴠᴧᴛєs ʀєᴘʟʏ ʀᴧɪᴅ
✧ {hl}ʀʀᴧɪᴅ &lt;ʀєᴘʟʏ&gt;
✧ {hl}ʀʀᴧɪᴅ &lt;υsєʀ&gt;
✧ {hl}ʜʀʀᴧɪᴅ &lt;ʀєᴘʟʏ&gt;
✧ {hl}ʜʀʀᴧɪᴅ &lt;υsєʀ&gt;</b>

<b>ᴅʀєᴘʟʏʀᴧɪᴅ: ᴅєᴧᴄᴛɪᴠᴧᴛєs ʀєᴘʟʏ ʀᴧɪᴅ
✧ {hl}ᴅʀʀᴧɪᴅ &lt;ʀєᴘʟʏ&gt;
✧ {hl}ᴅʀʀᴧɪᴅ &lt;υsєʀ&gt;
✧ {hl}ᴅʜʀᴧɪᴅ &lt;ʀєᴘʟʏ&gt;
✧ {hl}ᴅʜʀᴧɪᴅ &lt;υsєʀ&gt;</b>

<b>ʟσᴠє ʀᴧɪᴅ:
✧ {hl}ϻʀᴧɪᴅ &lt;ᴄσυηᴛ&gt; &lt;υsєʀ&gt;
✧ {hl}ʟσᴠєʀᴧɪᴅ &lt;ᴄσυηᴛ&gt; &lt;υsєʀ&gt;</b>

<b>ʜɪηᴅɪ ʀᴧɪᴅ:
✧ {hl}ʜʀᴧɪᴅ &lt;ᴄσυηᴛ&gt; &lt;υsєʀ&gt;
✧ {hl}ʜʀᴧɪᴅ &lt;ᴄσυηᴛ&gt; &lt;ʀєᴘʟʏ&gt;</b>

<b>ᴄʀᴧɪᴅ:
✧ {hl}ᴄʀᴧɪᴅ &lt;ᴄσυηᴛ&gt; &lt;υsєʀ&gt;
✧ {hl}ᴄʀᴧɪᴅ &lt;ᴄσυηᴛ&gt; &lt;ʀєᴘʟʏ&gt;</b>
"""


maanav_msg = f"""
<u><b>⫸ ηєᴡ ᴄσϻϻᴧηᴅs:</b></u>

<b>ɢσσᴅ ᴧғᴛєʀηση:
✧ {hl}ɢᴧ &lt;ᴄσυηᴛ&gt; &lt;υsєʀ&gt;
✧ {hl}ɢᴧ &lt;ᴄσυηᴛ&gt; &lt;ʀєᴘʟʏ&gt;</b>

<b>єϻσᴊɪ:
✧ {hl}єϻσᴊɪ &lt;ʀєᴘʟʏ&gt;
✧ {hl}єϻσᴊɪ &lt;υsєʀ&gt;</b>

<b>ɢσσᴅ ϻσʀηɪηɢ:
✧ {hl}ɢϻ &lt;ʀєᴘʟʏ&gt;
✧ {hl}ɢϻ &lt;υsєʀ&gt;</b>

<b>ɢσσᴅ ηɪɢʜᴛ:
✧ {hl}ɢη &lt;ᴄσυηᴛ&gt; &lt;υsєʀ&gt;
✧ {hl}ɢη &lt;ᴄσυηᴛ&gt; &lt;ʀєᴘʟʏ&gt;</b>

<b>sʜᴧʏʀɪ ʀᴧɪᴅ:
✧ {hl}sʀᴧɪᴅ &lt;ᴄσυηᴛ&gt; &lt;υsєʀ&gt;
✧ {hl}sʀᴧɪᴅ &lt;ᴄσυηᴛ&gt; &lt;ʀєᴘʟʏ&gt;</b>

<b>ғʟɪʀᴛ:
✧ {hl}ғʟɪʀᴛ &lt;ᴄσυηᴛ&gt; &lt;υsєʀ&gt;
✧ {hl}ғʟɪʀᴛ &lt;ᴄσυηᴛ&gt; &lt;ʀєᴘʟʏ&gt;</b>

<b>ʙɪʀᴛʜᴅᴧʏ:
✧ {hl}ʙsᴘᴧϻ &lt;ᴄσυηᴛ&gt; &lt;υsєʀ&gt;
✧ {hl}ʙsᴘᴧϻ &lt;ᴄσυηᴛ&gt; &lt;ʀєᴘʟʏ&gt;</b>
"""


spam_msg = f"""
<b><u>⫸ sᴘᴧϻ ᴄσϻϻᴧηᴅs:</u></b>

<b>sᴘᴧϻ:
✧ {hl}sᴘᴧϻ &lt;ᴄσυηᴛ&gt; &lt;ϻєssᴧɢє&gt;
✧ {hl}sᴘᴧϻ &lt;ᴄσυηᴛ&gt; &lt;ʀєᴘʟʏ&gt;</b>

<b>ᴘσʀηsᴘᴧϻ:
✧ {hl}ᴘsᴘᴧϻ &lt;ᴄσυηᴛ&gt;</b>

<b>ʜᴧηɢ:
✧ {hl}ʜᴧηɢ &lt;ᴄσυηᴛ&gt;</b>

<b>ᴧʙυsєsᴘᴧϻ:
✧ {hl}ᴧʙυsє &lt;ᴄσυηᴛ&gt; &lt;υsєʀ&gt;</b>
"""


@X1.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(
            HELP_STRING,
            buttons=[
              [
                Button.inline("sᴘᴧϻ", data="spam"),
                Button.inline("ʀᴧɪᴅ", data="raid")
              ],
              [
                Button.inline("ϻσʀє", data="moreaxiomcmd")
              ],
              [
                Button.inline("ηєᴡ ᴄσϻϻᴧηᴅ", data="maanav")
              ]
            ],
            parse_mode="html"
          )
    else:
        await event.answer("✧ ʏσυ ᴧʀє ησᴛ ᴧυᴛʜσʀɪᴢєᴅ ᴘʟєᴧsє ᴄσηᴛᴧᴄᴛ <a href='https://t.me/iii_maa7nav_iii/30'>ᴧxɪσϻ</a> ᴛσ ᴛᴧᴋє sυᴅσ ᴀᴄᴄєss", alert=True, parse_mode="html")


@X1.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(spam_msg,
              buttons=[[Button.inline("ʙᴧᴄᴋ ⟲", data="help_back"),],],
              parse_mode="html"
              ) 
    else:
        await event.answer("✧ ʏσυ ᴧʀє ησᴛ ᴧυᴛʜσʀɪᴢєᴅ ᴘʟєᴧsє ᴄσηᴛᴧᴄᴛ <a href='https://t.me/iii_maa7nav_iii/30'>ᴧxɪσϻ</a> ᴛσ ᴛᴧᴋє sυᴅσ ᴀᴄᴄєss", alert=True, parse_mode="html")


@X1.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg,
            buttons=[[Button.inline("ʙᴧᴄᴋ ⟲", data="help_back"),],],
            parse_mode="html"
          )
    else:
        await event.answer("✧ ʏσυ ᴧʀє ησᴛ ᴧυᴛʜσʀɪᴢєᴅ ᴘʟєᴧsє ᴄσηᴛᴧᴄᴛ <a href='https://t.me/iii_maa7nav_iii/30'>ᴧxɪσϻ</a> ᴛσ ᴛᴧᴋє sυᴅσ ᴀᴄᴄєss", alert=True, parse_mode="html")


@X1.on(events.CallbackQuery(pattern=r"moreaxiomcmd"))
async def help_moreaxiomcmd(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(moreaxiomcmd_msg,
            buttons=[[Button.inline("ʙᴧᴄᴋ ⟲", data="help_back"),],],
            parse_mode="html"
            )
    else:
        await event.answer("✧ ʏσυ ᴧʀє ησᴛ ᴧυᴛʜσʀɪᴢєᴅ ᴘʟєᴧsє ᴄσηᴛᴧᴄᴛ <a href='https://t.me/iii_maa7nav_iii/30'>ᴧxɪσϻ</a> ᴛσ ᴛᴧᴋє sυᴅσ ᴀᴄᴄєss", alert=True, parse_mode="html")
        
        
@X1.on(events.CallbackQuery(pattern=r"maanav"))
async def help_maanav(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(maanav_msg,
            buttons=[[Button.inline("ʙᴧᴄᴋ ⟲", data="help_back"),],],
            parse_mode="html"
            )
    else:
        await event.answer("✧ ʏσυ ᴧʀє ησᴛ ᴧυᴛʜσʀɪᴢєᴅ ᴘʟєᴧsє ᴄσηᴛᴧᴄᴛ <a href='https://t.me/iii_maa7nav_iii/30'>ᴧxɪσϻ</a> ᴛσ ᴛᴧᴋє sυᴅσ ᴀᴄᴄєss", alert=True, parse_mode="html")
