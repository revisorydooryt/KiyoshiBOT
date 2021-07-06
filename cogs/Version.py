import discord
from discord.ext import commands

class Version(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.command(name='version')
    async def version(self, ctx):

        verEmbed = discord.Embed(title="WeebBot's Details", description="The bot is in Version 1.0", color=0x69ff96)
        verEmbed.add_field(name="Version Code:", value="v1.0.0beta", inline=False)
        verEmbed.add_field(name="Date Released", value="12/23/2020", inline=False)
        verEmbed.set_footer(text="WeebBot is currently on Heavy Maintenance!")
        verEmbed.set_author(name="Created by xAlhanz04")

        await ctx.message.channel.send(embed=verEmbed)

def setup(bot):
    bot.add_cog(Version(bot))