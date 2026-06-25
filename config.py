import os

API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")

OWNER_ID = int(os.getenv("OWNER_ID", 0))
LOGGER_ID = int(os.getenv("LOGGER_ID", 0))

# Assistant Sessions
STRING1 = os.getenv("STRING1", "")
STRING2 = os.getenv("STRING2", "")
STRING3 = os.getenv("STRING3", "")
STRING4 = os.getenv("STRING4", "")
STRING5 = os.getenv("STRING5", "")

# Git Updater
GIT_TOKEN = os.getenv("GIT_TOKEN", "")

UPSTREAM_REPO = os.getenv(
    "UPSTREAM_REPO",
    "https://github.com/HMD7SLK/My_Sourcehmd"
)

UPSTREAM_BRANCH = os.getenv(
    "UPSTREAM_BRANCH",
    "master"
)
