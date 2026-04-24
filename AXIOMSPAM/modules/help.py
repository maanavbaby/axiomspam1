# © @III_MAA7NAV_III
from telethon import events, Button

from config import X1, SUDO_USERS, CMD_HNDLR as hl


HELP_STRING = f"<blockquote><b>📗 ᴅɪᴠє ɪηᴛσ ᴧʟʟ ᴄσϻϻᴧηᴅ ᴄᴧᴛєɢσʀɪєs ʙєʟσᴡ </blockquote>\n\n<blockquote>✧ ɢєᴛ ɢυɪᴅᴧηᴄє - ᴧssɪsᴛᴧηᴄє ɪη συʀ <a href='https://t.me/manavkiduniya'>sυᴘᴘσʀᴛ ᴄʜᴧᴛ</a> — ɪ'ϻ ʜєʀє ғσʀ ʏσυ!</b></blockquote>"

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
              has_spoiler=True,
              parse_mode="html",
              buttons=HELP_BUTTON
              )
        except Exception as e:
            await event.client.send_message(event.chat_id, f"<b>⫸ An Exception Occured!\n\n⫸ERROR: {str(e)}")


moreaxiomcmd_msg = f"""
<b><u>⫸ єxᴛʀᴧ  ᴄσϻϻᴧηᴅs:</u></b>

<blockquote><b>υsєʀʙσᴛ: υsєʀʙσᴛ ᴄϻᴅs
✧ {hl}ᴘɪηɢ
✧ {hl}ʀєʙσσᴛ
✧ {hl}sυᴅσ <ʀєᴘʟʏ ᴛσ υsєʀ>  --> ᴧxɪσϻ ᴄϻᴅ
✧ {hl}ʟσɢs --> ᴧxɪσϻ ᴄϻᴅ</b></blockquote>

<blockquote><b>єᴄʜσ: ᴛσ ᴧᴄᴛɪᴠє єᴄʜσ ση ᴧηʏ υsєʀ
✧ {hl}єᴄʜσ <ʀєᴘʟʏ ᴛσ υsєʀ>
✧ {hl}ʀϻєᴄʜσ <ʀєᴘʟʏ ᴛσ υsєʀ></b></blockquote>

<blockquote><b>ʟєᴧᴠє: ᴛσ ʟєᴧᴠє ɢʀσυᴘ/ᴄʜᴧηηєʟ
✧ {hl}ʟєᴧᴠє <ɢʀσυᴘ/ᴄʜᴧᴛ ɪᴅ>
✧ {hl}ʟєᴧᴠє : ᴛʏᴘє ɪη ᴛʜє ɢʀσυᴘ ʙσᴛ ᴡɪʟʟ ᴧυᴛσ ʟєᴧᴠє ᴛʜᴧᴛ ɢʀσυᴘ</b></blockquote>
"""


raid_msg = f"""
<u><b>⫸ ʀᴧɪᴅ ᴄσϻϻᴧηᴅs:</b></u>

<blockquote><b>ʀᴧɪᴅ: ᴧᴄᴛɪᴠᴧᴛєs ʀᴧɪᴅ ση ᴧηʏ ɪηᴅɪᴠɪᴅυᴧʟ υsєʀ ғσʀ ɢɪᴠєη ʀᴧηɢє
✧ {hl}ʀᴧɪᴅ <ᴄσυηᴛ> <υsєʀηᴧϻє>
✧ {hl}ʀᴧɪᴅ <ᴄσυηᴛ> <ʀєᴘʟʏ ᴛσ υsєʀ></b></blockquote>

<blockquote><b>ʀєᴘʟʏʀᴧɪᴅ: ᴧᴄᴛɪᴠᴧᴛєs ʀєᴘʟʏ ʀᴧɪᴅ
✧ {hl}ʀʀᴧɪᴅ <ʀєᴘʟʏ>
✧ {hl}ʀʀᴧɪᴅ <υsєʀ>
✧ {hl}ʜʀʀᴧɪᴅ <ʀєᴘʟʏ>
✧ {hl}ʜʀʀᴧɪᴅ <υsєʀ></b></blockquote>

<blockquote><b>ᴅʀєᴘʟʏʀᴧɪᴅ: ᴅєᴧᴄᴛɪᴠᴧᴛєs ʀєᴘʟʏ ʀᴧɪᴅ
✧ {hl}ᴅʀʀᴧɪᴅ <ʀєᴘʟʏ>
✧ {hl}ᴅʀʀᴧɪᴅ <υsєʀ>
✧ {hl}ᴅʜʀᴧɪᴅ <ʀєᴘʟʏ>
✧ {hl}ᴅʜʀᴧɪᴅ <υsєʀ></b></blockquote>

<blockquote><b>ʟσᴠє ʀᴧɪᴅ:
✧ {hl}ϻʀᴧɪᴅ <ᴄσυηᴛ> <υsєʀ>
✧ {hl}ʟσᴠєʀᴧɪᴅ <ᴄσυηᴛ> <υsєʀ></b></blockquote>

<blockquote><b>ʜɪηᴅɪ ʀᴧɪᴅ:
✧ {hl}ʜʀᴧɪᴅ <ᴄσυηᴛ> <υsєʀ>
✧ {hl}ʜʀᴧɪᴅ <ᴄσυηᴛ> <ʀєᴘʟʏ></b></blockquote>

<blockquote><b>ᴄʀᴧɪᴅ:
✧ {hl}ᴄʀᴧɪᴅ <ᴄσυηᴛ> <υsєʀ>
✧ {hl}ᴄʀᴧɪᴅ <ᴄσυηᴛ> <ʀєᴘʟʏ></b></blockquote>
"""


maanav_msg = f"""
<u><b>⫸ ηєᴡ ᴄσϻϻᴧηᴅs:</b></u>

<blockquote><b>ɢσσᴅ ᴧғᴛєʀηση:
✧ {hl}ɢᴧ <ᴄσυηᴛ> <υsєʀ>
✧ {hl}ɢᴧ <ᴄσυηᴛ> <ʀєᴘʟʏ></b></blockquote>

<blockquote><b>єϻσᴊɪ:
✧ {hl}єϻσᴊɪ <ʀєᴘʟʏ>
✧ {hl}єϻσᴊɪ <υsєʀ></b></blockquote>

<blockquote><b>ɢσσᴅ ϻσʀηɪηɢ:
✧ {hl}ɢϻ <ʀєᴘʟʏ>
✧ {hl}ɢϻ <υsєʀ></b></blockquote>

<blockquote><b>ɢσσᴅ ηɪɢʜᴛ:
✧ {hl}ɢη <ᴄσυηᴛ> <υsєʀ>
✧ {hl}ɢη <ᴄσυηᴛ> <ʀєᴘʟʏ></b></blockquote>

<blockquote><b>sʜᴧʏʀɪ ʀᴧɪᴅ:
✧ {hl}sʀᴧɪᴅ <ᴄσυηᴛ> <υsєʀ>
✧ {hl}sʀᴧɪᴅ <ᴄσυηᴛ> <ʀєᴘʟʏ></b></blockquote>

<blockquote><b>ғʟɪʀᴛ:
✧ {hl}ғʟɪʀᴛ <ᴄσυηᴛ> <υsєʀ>
✧ {hl}ғʟɪʀᴛ <ᴄσυηᴛ> <ʀєᴘʟʏ></b></blockquote>

<blockquote><b>ʙɪʀᴛʜᴅᴧʏ:
✧ {hl}ʙsᴘᴧϻ <ᴄσυηᴛ> <υsєʀ>
✧ {hl}ʙsᴘᴧϻ <ᴄσυηᴛ> <ʀєᴘʟʏ></b></blockquote>
"""


spam_msg = f"""
<b><u>⫸ sᴘᴧϻ ᴄσϻϻᴧηᴅs:</u></b>

<blockquote><b>sᴘᴧϻ:
✧ {hl}sᴘᴧϻ <ᴄσυηᴛ> <ϻєssᴧɢє>
✧ {hl}sᴘᴧϻ <ᴄσυηᴛ> <ʀєᴘʟʏ></b></blockquote>

<blockquote><b>ᴘσʀηsᴘᴧϻ:
✧ {hl}ᴘsᴘᴧϻ <ᴄσυηᴛ></b></blockquote>

<blockquote><b>ʜᴧηɢ:
✧ {hl}ʜᴧηɢ <ᴄσυηᴛ></b></blockquote>

<blockquote><b>ᴧʙυsєsᴘᴧϻ:
✧ {hl}ᴧʙυsє <ᴄσυηᴛ> <υsєʀ></b></blockquote>
  

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
            ]
          )
    else:
        await event.answer("✧ ʏσυ ᴧʀє ησᴛ ᴧυᴛʜσʀɪᴢєᴅ ᴘʟєᴧsє ᴄσηᴛᴧᴄᴛ <a href='https://t.me/iii_maa7nav_iii/30'>ᴧxɪσϻ</a> ᴛσ ᴛᴧᴋє sυᴅσ." , cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(spam_msg,
              buttons=[[Button.inline("ʙᴧᴄᴋ ⟲", data="help_back"),],],
              ) 
    else:
        await event.answer("✧ ʏσυ ᴧʀє ησᴛ ᴧυᴛʜσʀɪᴢєᴅ ᴘʟєᴧsє ᴄσηᴛᴧᴄᴛ <a href='https://t.me/iii_maa7nav_iii/30'>ᴧxɪσϻ</a> ᴛσ ᴛᴧᴋє sυᴅσ.", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg,
            buttons=[[Button.inline("ʙᴧᴄᴋ ⟲", data="help_back"),],],
          )
    else:
        await event.answer("✧ ʏσυ ᴧʀє ησᴛ ᴧυᴛʜσʀɪᴢєᴅ ᴘʟєᴧsє ᴄσηᴛᴧᴄᴛ <a href='https://t.me/iii_maa7nav_iii/30'>ᴧxɪσϻ</a> ᴛσ ᴛᴧᴋє sυᴅσ.", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"moreaxiomcmd"))
async def help_moreaxiomcmd(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(moreaxiomcmd_msg,
            buttons=[[Button.inline("ʙᴧᴄᴋ ⟲", data="help_back"),],],
            )
    else:
        await event.answer("✧ ʏσυ ᴧʀє ησᴛ ᴧυᴛʜσʀɪᴢєᴅ ᴘʟєᴧsє ᴄσηᴛᴧᴄᴛ <a href='https://t.me/iii_maa7nav_iii/30'>ᴧxɪσϻ</a> ᴛσ ᴛᴧᴋє sυᴅσ.", cache_time=0, alert=True)
        
        
@X1.on(events.CallbackQuery(pattern=r"maanav"))
async def help_maanav(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(maanav_msg,
            buttons=[[Button.inline("ʙᴧᴄᴋ ⟲", data="help_back"),],],
            )
    else:
        await event.answer("✧ ʏσυ ᴧʀє ησᴛ ᴧυᴛʜσʀɪᴢєᴅ ᴘʟєᴧsє ᴄσηᴛᴧᴄᴛ <a href='https://t.me/iii_maa7nav_iii/30'>ᴧxɪσϻ</a> ᴛσ ᴛᴧᴋє sυᴅσ.", cache_time=0, alert=True)
