from os import getenv

from decouple import config

APP_ID = getenv("APP_ID", "1945402")

API_HASH = getenv("API_HASH", "5fe8b55719270b8163bff9d32bdaaa78")

HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)

BOT_TOKEN = config("BOT_TOKEN", default=5765591009:AAH_3EezVnAq89Y0dAMbRNwL1uzBobMsCUk)
BOT_TOKEN2 = config("BOT_TOKEN2", default=6251600257:AAHwaoPzL23X7Exb2l6-P_WaD8bKDL50pL4)
BOT_TOKEN3 = config("BOT_TOKEN3", default=5886318269:AAECwLbBMMuqe7j_zj87kQqnYL94e_S4ZjY)
BOT_TOKEN4 = config("BOT_TOKEN4", default=5677671821:AAGL8uL_YZLShXpBZ9DXdtoVUTBXRlQhQoM)
BOT_TOKEN5 = config("BOT_TOKEN5", default=5678493977:AAGPWTlTqtKRIl1PKG9IovrCtUqI3VFv1Ak)
BOT_TOKEN6 = config("BOT_TOKEN6", default=5470518560:AAF3X0WKSS2bM3eAFVNtrYeJRe7bYNKhbOY)
BOT_TOKEN7 = config("BOT_TOKEN7", default=6153225183:AAGtCy87cph9JMbfr8tXhQHx_Gr4Sybg_fc)
BOT_TOKEN8 = config("BOT_TOKEN8", default=6054850344:AAGPbY388cKhfUxkvj869pEbNU4hECkVgKU)
BOT_TOKEN9 = config("BOT_TOKEN9", default=6152781098:AAHS9orsvvEqRYoEWYp4tNacq01ZtS_pChc)
BOT_TOKEN10 = config("BOT_TOKEN10", default=5937423293:AAGkWjaGaqB3tB-V7_LnI8Fx_6ngpGHvCWQ)
BOT_TOKEN11 = config("BOT_TOKEN11", default=None)
BOT_TOKEN12 = config("BOT_TOKEN12", default=None)
BOT_TOKEN13 = config("BOT_TOKEN13", default=None)
BOT_TOKEN14 = config("BOT_TOKEN14", default=None)
BOT_TOKEN15 = config("BOT_TOKEN15", default=None)
BOT_TOKEN16 = config("BOT_TOKEN16", default=None)
BOT_TOKEN17 = config("BOT_TOKEN17", default=None)
BOT_TOKEN18 = config("BOT_TOKEN18", default=None)
BOT_TOKEN19 = config("BOT_TOKEN19", default=None)
BOT_TOKEN20 = config("BOT_TOKEN20", default=None)
BOT_TOKEN21 = config("BOT_TOKEN21", default=None)
BOT_TOKEN22 = config("BOT_TOKEN22", default=None)
BOT_TOKEN23 = config("BOT_TOKEN23", default=None)
BOT_TOKEN24 = config("BOT_TOKEN24", default=None)
BOT_TOKEN25 = config("BOT_TOKEN25", default=None)
try:
    SUDO_USERS = str(getenv("SUDO_USERS", "5148516372")).split(" ")
except Exception:
    SUDO_USERS = str(getenv("SUDO_USERS", "5003311088"))

START_MESSAGE = getenv("START_MESSAGE", None)

PING_PIC = getenv("PING_PIC", None)

START_PIC = getenv("START_PIC", None)


HELP_MSG = getenv("HELP_MSG", None)
HELP_PIC = getenv("HELP_PIC", "https://graph.org/file/6b8349c4e936e0314d605.jpg")
LOG_CHANNEL = getenv("LOG_CHANNEL", None)

HANDLER = getenv("HANDLER", "/")
