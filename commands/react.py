import discord
from discord.ext import commands
from Core.classes import Cog_Extension
import random
import json

with open('setting.json','r',encoding='utf8') as jfile:  ##r=read
    jdata=json.load(jfile)

class React(Cog_Extension):

    @commands.command()
    async def web(self, ctx):
        random_pic=random.choice(jdata['url_pic'])
        await ctx.send(random_pic)

async def setup(bot):
    await bot.add_cog(React(bot))

