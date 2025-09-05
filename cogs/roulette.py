import discord
import random
import json
from discord.ext import commands

# IDs des propriétaires autorisés
OWNER_IDS = {199541824212172801, 512700060329443328}

class Roulette(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open("data/maps.json", "r", encoding="utf-8") as f:
            self.maps = json.load(f)["maps"]
        self.history = []

    @commands.command(name="roulette")
    async def roulette(self, ctx):
        """Tire UNE seule map aléatoire (accessible à tous)"""
        if not self.maps:
            await ctx.send("⚠️ Aucune map disponible.")
            return
        map_choice = random.choice(self.maps)
        self.history.append(map_choice)
        await ctx.send(f"🎲 La map tirée est : **{map_choice}**")

    @commands.command(name="excludemap")
    async def excludemap(self, ctx, *, map_name: str):
        """Exclut une map de la liste (OWNER uniquement)"""
        if ctx.author.id not in OWNER_IDS:
            await ctx.send("⛔ Tu n’as pas la permission d’exclure une map.")
            return

        map_name = map_name.strip().lower()
        maps_lower = [m.lower() for m in self.maps]

        if map_name in maps_lower:
            index = maps_lower.index(map_name)
            removed = self.maps.pop(index)
            await ctx.send(f"❌ La map **{removed}** a été exclue de la roulette.")
        else:
            await ctx.send(f"⚠️ La map **{map_name}** n’existe pas dans la liste.")

    @commands.command(name="addmap")
    async def addmap(self, ctx, *, map_name: str):
        """Ajoute une map à la liste (OWNER uniquement)"""
        if ctx.author.id not in OWNER_IDS:
            await ctx.send("⛔ Tu n’as pas la permission d’ajouter une map.")
            return

        map_name = map_name.strip()
        maps_lower = [m.lower() for m in self.maps]

        if map_name.lower() not in maps_lower:
            self.maps.append(map_name)
            await ctx.send(f"✅ La map **{map_name}** a été ajoutée.")
        else:
            await ctx.send(f"⚠️ La map **{map_name}** est déjà dans la liste.")

    @commands.command(name="history")
    async def history(self, ctx):
        """Affiche l’historique des tirages (accessible à tous)"""
        if self.history:
            history_str = ", ".join(self.history[-10:])
            await ctx.send(f"🕑 Historique des derniers tirages : {history_str}")
        else:
            await ctx.send("📭 Aucun tirage effectué pour le moment.")

    @commands.command(name="listmaps")
    async def listmaps(self, ctx):
        """Affiche toutes les maps disponibles (accessible à tous)"""
        if self.maps:
            maps_str = ", ".join(self.maps)
            await ctx.send(f"📋 Maps disponibles : {maps_str}")
        else:
            await ctx.send("📭 Aucune map n’est actuellement disponible.")

async def setup(bot):
    await bot.add_cog(Roulette(bot))
