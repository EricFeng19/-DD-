import discord
from discord.ext import commands

class Cog_Extension(commands.Cog):
    def __init__(self, bot, timeout=None):
        self.bot = bot
        self.timeout = timeout