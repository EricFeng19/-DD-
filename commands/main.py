import discord
from discord.ext import commands
from Core.classes import Cog_Extension

class Main(Cog_Extension):

    @commands.command()
    async def ping(self,ctx):  ##command綁ctx ctx=上下文 bot回復使用者下文
        await ctx.send(f"{round(self.bot.latency*1000)} (ms)") ##round 四捨五入
    
    @commands.command()
    async def em(self, ctx):
        embed=discord.Embed(title="About", url="https://www.youtube.com/@feng.N19/featured", description="早安安owo 這是我的機器人 還有歡迎訂閱我的Youtube頻道~~", color=0x2bc582)
        embed.set_author(name="印章Feng", url="https://www.youtube.com/@feng.N19/featured", icon_url="https://pa1.narvii.com/8153/dbdf83d929b6784ec7ba4fcf5bdfe6d16c767cf8r1-1280-1280_hq.gif")
        embed.set_thumbnail(url="https://static.tvtropes.org/pmwiki/pub/images/gura_oct2020_4.png")
        embed.add_field(name="5*5=?", value="35", inline=True)
        embed.add_field(name="Youtube頻道", value="印章Feng", inline=True)
        embed.set_footer(text="owo")
        await ctx.send(embed=embed)
    
    @commands.command()
    async def sayd(self, ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)
    
    @commands.command()
    async def clean(self, ctx, num: int):
        await ctx.channel.purge(limit=num+1)

async def setup(bot):
    await bot.add_cog(Main(bot))