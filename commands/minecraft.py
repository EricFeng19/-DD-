import discord
from discord.ext import commands
from Core.classes import Cog_Extension

import random
import json


with open('setting.json','r',encoding='utf8') as jfile:  
    jdata=json.load(jfile)

class Minecraft(Cog_Extension):

    @commands.command()
    async def rm1(self, ctx): #rm=random_minecraft
        random_mc=random.choice(jdata['Mincraft'])
        await ctx.send(random_mc)

    @commands.command()
    async def rm15(self, ctx): #rm=random_minecraft
        random_mc15=random.choices([(jdata['Mincraft'])], k=15)
        await ctx.send(random_mc15)


async def setup(bot):
    await bot.add_cog(Minecraft(bot))