import discord
import random
import json
from discord.ext import commands

class Roulette(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open("data/maps.json", "r", encoding="utf-8") as f:
            self.maps = json.load(f)["maps"]
        self.history = []

    @commands.command(name="roulette")
    async def roulette(self, ctx):
        """Tire UNE seule map aléatoire"""
        if not self.maps:
            await ctx.send("⚠️ Aucune map disponible.")
            return

        map_choice = random.choice(self.maps)
        self.history.append(map_choice)
        await ctx.send(f"🎲 La map tirée est : **{map_choice}**")

async def setup(bot):
    await bot.add_cog(Roulette(bot))
