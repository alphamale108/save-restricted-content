import os

# Bot token from @Botfather
BOT_TOKEN = os.environ["BOT_TOKEN"]

# Your API ID from my.telegram.org
API_ID = int(os.environ["API_ID"])

# Your API Hash from my.telegram.org
API_HASH = os.environ["API_HASH"]

# Your Owner / Admin ID for Broadcast
ADMINS = int(os.environ["ADMINS"])

# Your MongoDB Database URL
DB_URI = os.environ["DB_URI"]
DB_NAME = os.environ["DB_NAME"]

# If you want error messages in your personal messages, set to True; otherwise, False
ERROR_MESSAGE = bool(os.environ.get("ERROR_MESSAGE"))
