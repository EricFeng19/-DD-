import discord
from discord.ext import commands

import json, os

with open('setting.json','r',encoding='utf8') as jfile:  #r=read
    jdata=json.load(jfile)

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='f!',help_command=None, intents=discord.Intents.all())

    async def setup_hook(self):
        for filename in os.listdir('./commands'): #./相對路徑
            if filename.endswith('.py'):
                await self.load_extension(f'commands.{filename[:-3]}') #ex:main.py 系統會把後三位.py自動刪除 避免出bug

    async def on_ready(self):
        print(f'目前登入機器人｜{self.user}')          

if __name__ == "__main__":
    MyBot().run(jdata['TOKEN'])