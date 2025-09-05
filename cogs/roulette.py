import discord
import random
import json
import os
import sys
from discord.ext import commands

# Remplace par TON ID DISCORD (clic droit sur ton profil > Copier l'identifiant)
OWNER_ID = 199541824212172801  

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

    @commands.command(name="excludemap")
    async def excludemap(self, ctx, *, map_name: str):
        """Exclut une map de la liste"""
        map_name = map_name.strip()
        if map_name in self.maps:
            self.maps.remove(map_name)
            await ctx.send(f"❌ La map **{map_name}** a été exclue de la roulette.")
        else:
            await ctx.send(f"⚠️ La map **{map_name}** n’existe pas ou est déjà exclue.")

    @commands.command(name="addmap")
    async def addmap(self, ctx, *, map_name: str):
        """Ajoute une map à la liste"""
        map_name = map_name.strip()
        if map_name not in self.maps:
            self.maps.append(map_name)
            await ctx.send(f"✅ La map **{map_name}** a été ajoutée.")
        else:
            await ctx.send(f"⚠️ La map **{map_name}** est déjà dans la liste.")

    @commands.command(name="history")
    async def history(self, ctx):
        """Affiche l’historique des tirages"""
        if self.history:
            history_str = ", ".join(self.history[-10:])
            await ctx.send(f"🕑 Historique des derniers tirages : {history_str}")
        else:
            await ctx.send("📭 Aucun tirage effectué pour le moment.")

    @commands.command(name="listmaps")
    async def listmaps(self, ctx):
        """Affiche toutes les maps disponibles"""
        if self.maps:
            maps_str = ", ".join(self.maps)
            await ctx.send(f"📋 Maps disponibles : {maps_str}")
        else:
            await ctx.send("📭 Aucune map n’est actuellement disponible.")

    @commands.command(name="reboot")
    async def reboot(self, ctx):
        """Redémarre le bot (réservé au propriétaire)"""
        if ctx.author.id != OWNER_ID:
            await ctx.send("⛔ Tu n’as pas la permission de redémarrer le bot.")
            return

        await ctx.send("🔄 Redémarrage en cours...")
        await self.bot.close()
        os.execv(sys.executable, ["python"] + sys.argv)

async def setup(bot):
    await bot.add_cog(Roulette(bot))
