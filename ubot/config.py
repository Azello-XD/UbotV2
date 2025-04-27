import os
from dotenv import load_dotenv

load_dotenv()

DEVS = [
    1927018403,
    1927018403,
]

KYNAN = list(
    map(
        int,
        os.getenv(
            "JONATHAN",
            "1927018403",
        ).split(),
    )
)

API_ID = int(os.getenv("API_ID", "27418440"))

API_HASH = os.getenv("API_HASH", "0a08a360e0e9f41b9896f655c300d09d")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7363561894:AAEAlRcisKQC_MaoACtlcA9vKJs8ZUVCc6U")

OWNER_ID = int(os.getenv("OWNER_ID", "1927018403"))


USER_ID = list(
    map(
        int,
        os.getenv(
            "USER_ID",
            "1927018403 1927018403",
        ).split(),
    )
)

LOG_UBOT = int(os.getenv("LOG_UBOT", "-1002584508663"))

LOG_SELLER = int(os.getenv("LOG_SELLER", "-1002614779233"))

BLACKLIST_CHAT = list(
    map(
        int,
        os.getenv(
            "BLACKLIST_CHAT",
            "-1001794660377 -1001759323059 -4006807112 -1002094957966 -1002106238548 -1001908722151 -1001812143750",
        ).split(),
    )
)

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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",
).split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://wtfbruh:KontolXD#123@fsub.brzgete.mongodb.net/?retryWrites=true&w=majority&appName=fsub",
)

DB_NAME = os.getenv("DB_NAME", "mongo.xyraacode")
