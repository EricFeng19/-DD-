import discord
from discord.ext import commands
from Core.classes import Cog_Extension

class Help(Cog_Extension):
    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        embed=discord.Embed(title="印章的DD機器人~~help指令說明", description="有關機器人的所有指令(´∀`)", color=0x57c164)
        embed.set_author(name="印章Feng", url="https://www.youtube.com/@feng.N19/featured")
        embed.add_field(name="title", value="細項說明 (〜-ω-)〜", inline=False)
        embed.add_field(name="main", value="DD機器人的主要工作", inline=True)
        embed.add_field(name="minecraft", value="可以隨機選擇一個麥塊的物品！", inline=False)
        embed.add_field(name="react", value="讓機器人回覆你的需求~", inline=True)
        embed.add_field(name="game", value="來玩一些印章編寫的酷酷的小遊戲uwu", inline=False)
        embed.add_field(name="尚待更新", value="拿起槌子敲印章 請他趕緊更新更多的指令(`Д´)（如果是Nitro效果更佳AwA）", inline=False)
        embed.set_footer(text="請使用f!help title  (如f!help game) 繼續查詢細項指令~")
        await ctx.send(embed=embed)

    @help.command()
    async def game(self, ctx):
        embed=discord.Embed(title="印章的DD機器人~~所有game指令說明", description="有關機器人的小遊戲(´∀`)", color=0x57c164)
        embed.add_field(name="title", value="細項說明 (〜-ω-)〜", inline=False)
        embed.add_field(name="guess", value="猜數字小遊戲！", inline=True)
        embed.set_footer(text="請使用f!help title  (如f!help guess) 繼續查詢其他小遊戲玩法~")
        await ctx.send(embed=embed)

    @help.command()
    async def guess(self, ctx):
        embed=discord.Embed(title="印章的DD機器人<-<guess>->小遊戲指令說明", description="猜數字(つ´ω`)つ", color=0x57c164)
        embed.add_field(name="gamerole", value="規則說明 (〜-ω-)〜", inline=False)
        embed.add_field(name="數字範圍", value="1~100內的正整數", inline=False)
        embed.add_field(name="遊戲特色", value="會幫你紀錄猜測次數 歡迎跟其他人比比運氣owo", inline=True)
        embed.set_footer(text="請使用f!guess開始遊玩,或是輸入f!help 回到首頁")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))