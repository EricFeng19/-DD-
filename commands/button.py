import discord
from discord.ext import commands
from Core.classes import Cog_Extension

class Button(Cog_Extension,discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    def __init__(self):
        super().__init__(timeout=None)  # 調用父類的初始化方法

    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.blurple) # Create a button with the label "Click me!" with color Blurple
    async def callback(self, interaction:discord.interactions, Button:discord.ui.Button):
        await interaction.response.send(f'You clicked the button!') # Send a message when the button is clicked

    @commands.command(name = "buttonmenu") 
    async def buttonmenu(self, ctx):
        await ctx.respond(f'This is a button!', view = Button()) # Send a message with our View class that contains the button

async def setup(bot):
    await bot.add_cog(Button(bot))