import discord
from discord.ext import commands
from Core.classes import Cog_Extension
import json

with open('setting.json','r',encoding='utf8') as jfile:  ##r=read
    jdata=json.load(jfile)

class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['welcome_channel']))
        await channel.send(f'歡迎 {member.mention} 加入此伺服器!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['leave_channel']))
        await channel.send(f'{member.mention} 離開了!')

    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword = ['印章','嗨','eric']
        if msg.content in keyword and msg.author !=self.bot.user: #== '印章'
            await msg.channel.send('嗨')

async def setup(bot):
    await bot.add_cog(Event(bot))