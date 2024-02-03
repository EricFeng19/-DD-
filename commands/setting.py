import discord
from discord.ext import commands
from Core.classes import Cog_Extension

# 不需要定義 bot

class Setting(Cog_Extension):
    @commands.command()
    async def load(self, ctx, extension):
        await self.bot.load_extension(f'commands.{extension}') # self.bot
        await ctx.send(f'Loaded {extension} done.')

    @commands.command()
    async def unload(self, ctx, extension):
        await self.bot.unload_extension(f'commands.{extension}') # self.bot
        await ctx.send(f'Un - Loaded {extension} done.') 
        
    @commands.command()
    async def reload(self, ctx, extension):
        await self.bot.reload_extension(f'commands.{extension}') # self.bot
        await ctx.send(f'Re - Loaded {extension} done.')
        
async def setup(bot):
    await bot.add_cog(Setting(bot))