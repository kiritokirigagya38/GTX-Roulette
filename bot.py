import discord
import json
import asyncio
import os
import threading
from discord.ext import commands
from dotenv import load_dotenv
from flask import Flask

# Charger les variables d'environnement
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Charger la config
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

intents = discord.Intents.default()
bot = commands.Bot(command_prefix=config["prefix"], intents=intents)

# Charger les cogs
async def load_cogs():
    await bot.load_extension("cogs.roulette")

@bot.event
async def on_ready():
    print(f"⚜️ Connecté en tant que {bot.user}")

# --- Serveur web Flask ---
app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Bot Valorant Roulette est en ligne !"

def run_web():
    port = int(os.environ.get("PORT", 8080))  # Render fournit la variable PORT
    app.run(host="0.0.0.0", port=port)

# Lancer Flask dans un thread séparé
threading.Thread(target=run_web).start()

# --- Lancer le bot Discord ---
async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

asyncio.run(main())
