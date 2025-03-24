from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
BOT_TOKEN = getenv("BOT_TOKEN"), "7176335716:AAHixrnDSA42sPW_9jfYc5RdwoWx_LzcQMc"))
API_ID = int(getenv("API_ID", "24669465"))
API_HASH = getenv("API_HASH"), "ef15199702ea76ebb2ebe4eca477ab60"))
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "10"))
MONGO_DB_URI = getenv("MONGO_DB_URI"), "mongodb+srv://cenap526:cenappp526@cluster0.7onsb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "6623140842").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002662249469"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/jankarikiduniya/TG-Music")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

if str(getenv("SUPPORT_CHANNEL")).strip() == "https://t.me/+WWX0t-5B509iMWE0":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP")).strip() == "@Turkiyelinki":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))


if str(getenv("STRING_SESSION1")).strip() == "BAF4bRkAmZqo6k7_HacnAbxm2-wU1_sHt3eSYofTxeo9tHOWq1u55UYhDNwv-0FUp9LJdjFbK0ch7rUVupCa-vbUNIUXfUZLZy6h3y5xJzHrEWe_tF4rxYLo2PXI6MoECbw14_J49pt0djDq3hzqRP4rsFwWBFOK421w0-O9_0Evbs-Gg0Tj6HAC3k-lGFp3d8w8DGmMLmh-vyZZVv2bZSj1EQLPjKD0Pv8PCMKLYMT_-b81IBWNbLzJWuF9Q2JPhgGeuqkRgA6O-AbNVT_oGQBsAe8UxhAVlRz-Rs61inueDuOWmILQddH0snFFGTx53BHT5wiuwaHr38sWCg_uXdo7ER9fhwAAAAG_f8l8AA":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("STRING_SESSION1"))

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(None)
else:
    STRING5 = str(getenv("STRING_SESSION5"))

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("LOG_SESSION"))
