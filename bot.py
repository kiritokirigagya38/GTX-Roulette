import discord
import json
import asyncio
import os
import sys
from discord.ext import commands
from dotenv import load_dotenv

# Charger variables d'environnement
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

# Fichier pour stocker le dernier salon
LAST_CHANNEL_FILE = "last_channel.json"

def save_last_channel(channel_id: int):
    with open(LAST_CHANNEL_FILE, "w", encoding="utf-8") as f:
        json.dump({"channel_id": channel_id}, f)

def load_last_channel():
    if os.path.exists(LAST_CHANNEL_FILE):
        with open(LAST_CHANNEL_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("channel_id")
    return None

@bot.event
async def on_ready():
    print(f"⚜️ Connecté en tant que {bot.user}")

    # Charger le dernier salon utilisé
    last_channel_id = load_last_channel()
    if last_channel_id:
        channel = bot.get_channel(last_channel_id)
        if channel:
            await channel.send("✅ Le bot est de retour en ligne et prêt à rouler 🎲 !")

# ✅ Commande reboot stable
@bot.command(name="reboot")
async def reboot(ctx):
    """Redémarre le bot (réservé aux propriétaires)"""
    if ctx.author.id not in OWNER_IDS:
        await ctx.send("⛔ Tu n’as pas la permission de redémarrer le bot.")
        return

    # Sauvegarder le salon avant de quitter
    save_last_channel(ctx.channel.id)

    await ctx.send("🔄 Redémarrage en cours...")
    await bot.close()
    sys.exit(0)

async def main():
    async with bot:
        if "cogs.roulette" not in bot.extensions:
            await bot.load_extension("cogs.roulette")
            print("✅ Cog 'roulette' chargé")
        else:
            print("⚠️ Cog 'roulette' déjà chargé, ignoré")

        await bot.start(TOKEN)

asyncio.run(main())
