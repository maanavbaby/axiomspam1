import logging

from telethon import TelegramClient

from os import getenv
from AXIOMSPAM.data import AXIOMM


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR AXIOMSPAMBOT
API_ID = 39930006
API_HASH = "0c1afd87f1a69d0e9a8b06b779480f51"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

BOT_TOKEN = getenv("BOT_TOKEN", default="8736309668:AAEXZiz8Stu9w2t4GGoIkCibIaq8Nc_5cDI")

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="8466540017").split()))
for x in AXIOMM:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="7169279112"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
