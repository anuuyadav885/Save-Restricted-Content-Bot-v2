# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "24509126"))
API_HASH = getenv("API_HASH", "2c1e3e02b9e1b0a3f9c7955d5d55a1d5")
BOT_TOKEN = getenv("BOT_TOKEN", "7408929096:AAHcZslYiZNMa9xoDP-Qa10wIOeOQOoF-BA")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6127347210").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://codaga9286:JgH1nbOW5JSXUO4U@cluster0.if4xdya.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002584614736")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002630069470"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "500"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "10000"))
WEBSITE_URL = getenv("WEBSITE_URL", "modijiurl.com")
AD_API = getenv("AD_API", "71d8d386c59be6d3190202f69ff68e182c17bceb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
