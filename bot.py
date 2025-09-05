import discord
import json
import os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Charger config.json
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# Intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=config["prefix"], intents=intents)

@bot.event
async def on_ready():
    print(f"⚜️ Connecté en tant que {bot.user}")

async def main():
    async with bot:
        # ⚠️ Charger le cog UNE seule fois
        await bot.load_extension("cogs.roulette")
        await bot.start(TOKEN)

asyncio.run(main())
