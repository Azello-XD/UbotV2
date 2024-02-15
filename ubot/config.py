import os
from dotenv import load_dotenv

load_dotenv()

DEVS = [
    5832742519,
    6504480848,
]

KYNAN = list(
    map(
        int,
        os.getenv(
            "KYNAN",
            "5832742519",
        ).split(),
    )
)

API_ID = int(os.getenv("API_ID", "26979834"))

API_HASH = os.getenv("API_HASH", "546d1227a68ebabbfce69ba22a0e0127")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6458030143:AAFkwVsh9A2y47T0Bgw3b6o1u4KH3hPQ-gk")

OWNER_ID = int(os.getenv("OWNER_ID", "5832742519"))

USER_ID = list(
    map(
        int,
        os.getenv(
            "USER_ID",
            "5832742519 6504480848",
        ).split(),
    )
)

LOG_UBOT = int(os.getenv("LOG_UBOT", "-1002058883544"))

LOG_SELLER = int(os.getenv("LOG_SELLER", "-100205888354"))

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
    "mongodb+srv://jvbt:jvbt@cluster0.fqhgdcp.mongodb.net/?retryWrites=true&w=majority",
)

DB_NAME = os.getenv("DB_NAME", "mongo.skyubot")
