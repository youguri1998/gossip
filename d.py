import requests, sqlite3, telepot, os
from dotenv import load_dotenv

load_dotenv()
bot_token = os.getenv("my_token")
channel_id = os.getenv("me")
print(bot_token,'\n', channel_id)
bot = telepot.Bot(bot_token)

bot.sendMessage(channel_id, "Hello, World!")