from YousefMusic.core.bot import Zelzaly
from YousefMusic.core.dir import dirr
from YousefMusic.core.git import git
from YousefMusic.core.userbot import Userbot

from .logging import LOGGER

dirr()
git()

app = Zelzaly()
userbot = Userbot()

from YousefMusic.platforms.Youtube import YouTubeAPI

YouTube = YouTubeAPI()

Compatibility variables for old plugins

Apple = None
Resso = None
SoundCloud = None
Spotify = None
Telegram = None
