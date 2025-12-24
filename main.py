import discord
import os
from discord.ext import commands
from discord import app_commands
from database import get_database_instance
from pymongo import MongoClient
from dotenv import load_dotenv
from keep_alive import keep_alive 

load_dotenv()
token = os.environ.get("DISCORD_TOKEN")
mongo_url = os.environ.get("MONGO_URL")

cluster = MongoClient(mongo_url)
db = cluster["MiBaseDeDatos"]
collection = db["Usuarios"]

class MyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)
        self.db = get_database_instance()

    async def setup_hook(self):
        #aqui comandos de barra con el self db y el otro self
        await self.tree.sync()

bot = MyBot()


@bot.event
async def on_ready():
    print(f'Logueado como {bot.user}')

keep_alive()
bot.run(os.environ.get("DISCORD_TOKEN"))