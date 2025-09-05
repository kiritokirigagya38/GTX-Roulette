import discord
import json
import asyncio
import os
import sys
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

# IDs des propriétaires autorisés
OWNER_IDS = {199541824212172801, 512700060329443328}

@bot.event
async def on_ready():
    print(f"⚜️ Connecté en tant que {bot.user}")

# ✅ Commande reboot gérée directement dans bot.py
@bot.command(name="reboot")
async def reboot(ctx):
    """Redémarre le bot (réservé aux propriétaires)"""
    if ctx.author.id not in OWNER_IDS:
        await ctx.send("⛔ Tu n’as pas la permission de redémarrer le bot.")
        return

    await ctx.send("🔄 Redémarrage en cours...")
    await bot.close()
    sys.exit(0)  # L’hébergeur relancera automatiquement le process

async def main():
    async with bot:
        if "cogs.roulette" not in bot.extensions:
            await bot.load_extension("cogs.roulette")
            print("✅ Cog 'roulette' chargé")
        else:
            print("⚠️ Cog 'roulette' déjà chargé, ignoré")

        await bot.start(TOKEN)

asyncio.run(main())
