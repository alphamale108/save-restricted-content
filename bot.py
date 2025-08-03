# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from pyrogram import Client
import os
from config import API_ID, API_HASH, BOT_TOKEN

class Bot(Client):

    def __init__(self):
        try:
            super().__init__(
                "techvj_login",
                api_id=API_ID,
                api_hash=API_HASH,
                bot_token=BOT_TOKEN,
                plugins=dict(root="TechVJ"),
                workers=50,
                sleep_threshold=10
            )
        except KeyError as e:
            print(f"Error: Missing environment variable {e}. Please set all required environment variables (BOT_TOKEN, API_ID, API_HASH).")
            raise

    async def start(self):
        try:
            await super().start()
            print('Bot Started Powered By Jashey')
        except Exception as e:
            print(f"Error starting bot: {e}")
            raise

    async def stop(self, *args):
        await super().stop()
        print('Bot Stopped Bye')

if __name__ == "__main__":
    try:
        Bot().run()
    except Exception as e:
        print(f"Fatal error: {e}")

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
