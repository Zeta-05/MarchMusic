import re
from dotenv import load_dotenv
from pyrogram import filters
load_dotenv()

# Function to clean and convert environment variables to integers safely
def clean_int(value, default=0):
    try:
        return int(str(value).strip().replace("\u200e", ""))
    except ValueError:
        return default

# Get values from environment variables
API_ID = "12345678"
API_HASH = "f4ke90hash0000example9999"
BOT_TOKEN = "9999999999:AAFakeBotTokenExample0000"
MONGO_DB_URI = "mongodb+srv://username:password@cluster0.mongodb.net/?retryWrites=true&w=majority"

DURATION_LIMIT_MIN = clean_int(os.getenv("DURATION_LIMIT", 60000))
ADS_MODE = os.getenv("ADS_MODE", None)
LOGGER_ID = clean_int(os.getenv("LOGGER_ID", "-1001234567890"))
OWNER_ID = clean_int(os.getenv("OWNER_ID", "1234567890"))

# Heroku Configs
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", "fake-heroku-app")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY", "fakeherokuapikey000000")

# API URLs
API_URL = 'https://pytdbotapi.fakeapi.xyz'  # youtube song url
VIDEO_API_URL = "https://api.video.fakeapi.xyz"
API_KEY = "FAKEAPIKEY-00000-EXAMPLE-12345"  # fake youtube song api key

# Repository Information
UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/example/FakeMusicBot")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = os.getenv("GIT_TOKEN", "fakegitkey000000")

# Telegram Support & Channels
SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/FakeSupportChannel")
SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "https://t.me/FakeSupportGroup")

AUTO_LEAVING_ASSISTANT = bool(os.getenv("AUTO_LEAVING_ASSISTANT", None))

# Spotify API Credentials
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "fake_spotify_id")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "fake_spotify_secret")

# Playlist Limits
PLAYLIST_FETCH_LIMIT = clean_int(os.getenv("PLAYLIST_FETCH_LIMIT", 25))

# Telegram File Size Limits (in bytes)
TG_AUDIO_FILESIZE_LIMIT = clean_int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = clean_int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

# Pyrogram Session Strings (FAKE)
STRING1 = "BQFakeSessionExampleString0000"
STRING2 = os.getenv("STRING_SESSION2", "BQFakeSessionExample2")
STRING3 = os.getenv("STRING_SESSION3", None)
STRING4 = os.getenv("STRING_SESSION4", None)
STRING5 = os.getenv("STRING_SESSION5", None)

# Banned Users & Other Variables
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Image & Video URLs
START_VIDEO_URL = os.getenv("START_VIDEO_URL", "https://files.catbox.moe/fakevideo.mp4")
START_IMG_URL = os.getenv("START_IMG_URL", "https://files.catbox.moe/fakeimage.jpg")
PING_IMG_URL = os.getenv("PING_IMG_URL", "https://files.catbox.moe/fakeimage.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/fakeimage.jpg"
STATS_IMG_URL = "https://files.catbox.moe/fakeimage.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/fakeimage.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/fakeimage.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/fakeimage.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/fakeimage.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/fakeimage.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/fakeimage.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/fakeimage.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/fakeimage.jpg"

# Convert time format (hh:mm:ss) to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

# Validate URLs
if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL URL is incorrect. It must start with https://")

if SUPPORT_CHAT and not re.match("(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Your SUPPORT_CHAT URL is incorrect. It must start with https://") to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Auto Gcast/Broadcast Handler (True = broadcast on , False = broadcast off During Hosting, Dont Do anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "bcfe26b0ebc3428882a0b5fb3e872473")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "907c6a054c214005aeae1fd752273cc4")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "2000"))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @BRANDEDSTRINGSESSION_BOT on Telegram
STRING1 = getenv("STRING_SESSION",  None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/62c76ac2095332a0ede75.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/4f59fb748e1990acfa297.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/14eb59ea7d31229d8d751.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/4310ea5f523520b2b765b.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/923c1faac33d8c70335dc.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6c66f8b192532fe758e82.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/ebc4dc6357be06e08a3ed.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/d339f390ec168c19879c6.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/ee0cd53ab73f08f4a3627.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/5f9fb5bba66021c782d96.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/affe0afec5c7ad63676a4.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/3c446e8dee78ed0ca62ff.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
