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
        """Tire une map aléatoire"""
        map_choice = random.choice(self.maps)
        self.history.append(map_choice)
        await ctx.send(f"🎲 La map tirée est : **{map_choice}**")

    @commands.command(name="excludemap")
    async def excludemap(self, ctx, *, map_name: str):
        """Exclut une map de la roulette"""
        if map_name in self.maps:
            self.maps.remove(map_name)
            await ctx.send(f"❌ La map **{map_name}** a été exclue.")
        else:
            await ctx.send("⚠️ Cette map n’existe pas ou est déjà exclue.")

    @commands.command(name="addmap")
    async def addmap(self, ctx, *, map_name: str):
        """Ajoute une map à la roulette"""
        if map_name not in self.maps:
            self.maps.append(map_name)
            await ctx.send(f"✅ La map **{map_name}** a été ajoutée.")
        else:
            await ctx.send("⚠️ Cette map est déjà dans la liste.")

    @commands.command(name="history")
    async def history(self, ctx):
        """Affiche l’historique des maps tirées"""
        if self.history:
            history_str = ", ".join(self.history[-10:])
            await ctx.send(f"🕑 Historique récent : {history_str}")
        else:
            await ctx.send("📭 Aucun tirage pour le moment.")

async def setup(bot):
    await bot.add_cog(Roulette(bot))
