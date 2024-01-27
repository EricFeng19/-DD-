import discord
from discord.ext import commands, tasks
from Core.classes import Cog_Extension
import json, asyncio, datetime

class Task(Cog_Extension):
    @tasks.loop(seconds=5)
    async def say_hi(self):
      channel = self.get_channel(1031973964291002399)
      await channel.send("Hi I'm here owo")

    @tasks.loop(seconds=15)
    async def say_task(self):
      channel = self.get_channel(1031973964291002399)
      now_time = datetime.datetime.now().strftime('%H%M')
      with open('setting.json','r',encoding='utf8') as jfile: #r=read
          jdata = json.load(jfile)
      if now_time == jdata['time']:
          await channel.send('Task Working!')

    @commands.command()
    async def set_channel(self, ctx, ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set Channel:{self.channel.mention}')

    @commands.command()
    async def set_time(self, ctx, time):
        with open('setting.json','r',encoding='utf8') as jfile: #r=read
            jdata = json.load(jfile)
        jdata['time']=time
        with open('setting.json','w',encoding='utf8') as jfile: #w=write
            jdata.dump(jdata,jfile,indent=4)

async def setup(bot):
    await bot.add_cog(Task(bot))