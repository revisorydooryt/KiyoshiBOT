import discord
from discord.ext import commands

import random

from discord.ext.commands import bot

class Games(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='roll')
    async def roll(self, ctx):

        value = random.randint(0,100)
        await ctx.send(ctx.message.author.mention + f"-chang rolled {value}!")

def setup(bot):
    bot.add_cog(Games(bot))