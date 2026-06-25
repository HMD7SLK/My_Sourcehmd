import os

API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")

OWNER_ID = int(os.getenv("OWNER_ID", 0))

STRING1 = os.getenv("STRING1", "")
STRING2 = os.getenv("STRING2", "")
STRING_SESSION = os.getenv("STRING_SESSION", "")

LOGGER_ID = int(os.getenv("LOGGER_ID", 0))

GIT_TOKEN = os.getenv("GIT_TOKEN", "")

UPSTREAM_REPO = os.getenv(
    "UPSTREAM_REPO",
    "https://github.com/HMD7SLK/My_Sourcehmd"
)

UPSTREAM_BRANCH = os.getenv(
    "UPSTREAM_BRANCH",
    "master"
)
