import discord
from discord.ext import commands
from Core.classes import Cog_Extension

class Button(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View

    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.primary) # Create a button with the label "Click me!" with color Blurple
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("You clicked the button!") # Send a message when the button is clicked

    @commands.slash() 
    async def button(ctx):
        await ctx.respond("This is a button!", view=Button()) # Send a message with our View class that contains the button

async def setup(bot):
    await bot.add_cog(Button(bot))