import discord
import json
import asyncio
import os
from discord.ext import commands
from dotenv import load_dotenv

# Charger les variables d'environnement (.env ou Render env)
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Charger la config
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# --- Intents (obligatoire pour lire les messages) ---
intents = discord.Intents.default()
intents.message_content = True  # ⚠️ Indispensable pour les commandes

bot = commands.Bot(command_prefix=config["prefix"], intents=intents)

# --- Charger les cogs ---
async def load_cogs():
    await bot.load_extension("cogs.roulette")

@bot.event
async def on_ready():
    print(f"⚜️ Connecté en tant que {bot.user}")

# --- Lancement du bot ---
async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

asyncio.run(main())
