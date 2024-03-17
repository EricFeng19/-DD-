import discord
from discord.ext import commands
from Core.classes import Cog_Extension
import json

# 讀取(r=read) setting.json 檔案，並轉換為 Python 物件(class)
with open('setting.json','r',encoding='utf8') as jfile: 
    jdata=json.load(jfile)

class Event(Cog_Extension): # 從之前導入的 Cog_Extension 定義一個名為 Event 的類別 

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