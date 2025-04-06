import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(os.getenv("MTMxNDg3NTQ0MTE2ODkxMjQwNA.GZSldP.3R2h-7Wkynz_igYH98byzTJk_YDEHCiCPeqU_g"))
