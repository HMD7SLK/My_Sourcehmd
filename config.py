import os
from pyrogram import filters

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

SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "ZThon")
CH_US = os.getenv("CH_US", "ZThon")

adminlist = {}
confirmer = {}
votemode = {}
autoclean = []

# Images
YOUTUBE_IMG_URL = "https://telegra.ph/file/cc0a0c2d8f5e4f0d3f5d1.jpg"
STREAM_IMG_URL = YOUTUBE_IMG_URL
SOUNDCLOUD_IMG_URL = YOUTUBE_IMG_URL
TELEGRAM_AUDIO_URL = YOUTUBE_IMG_URL
TELEGRAM_VIDEO_URL = YOUTUBE_IMG_URL

# Images
START_IMG_URL = YOUTUBE_IMG_URL
PING_IMG_URL = YOUTUBE_IMG_URL
PLAYLIST_IMG_URL = YOUTUBE_IMG_URL
GLOBAL_IMG_URL = YOUTUBE_IMG_URL
STATS_IMG_URL = YOUTUBE_IMG_URL

# Assistant
AUTO_LEAVING_ASSISTANT = False
AUTO_DOWNLOADS_CLEAR = False
AUTO_SUGGESTION_MODE = False

# Support
SUPPORT_GROUP = "https://t.me/ZThon"
SUPPORT_CHANNEL = "https://t.me/Zelzal_Music"

# Yafa
YAFA_CHANNEL = "ZThon"
YAFA_NAME = "ZThon"
CHANNEL_SUDO = OWNER_ID
