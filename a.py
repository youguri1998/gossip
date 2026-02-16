from dotenv import load_dotenv
import os, telepot

load_dotenv()

me = os.getenv("me")


bot = telepot.Bot(os.getenv("token"))
bot.sendMessage(me, "Hello, World!")

