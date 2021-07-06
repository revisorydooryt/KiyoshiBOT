from datetime import datetime

import discord
from discord.ext import commands

import sys
import psutil

class System(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.launch_time = datetime.utcnow()

    @commands.Cog.listener()
    async def on_ready(self):
        print('Kiyoshi is online!')

        await self.bot.change_presence(status=discord.Status.idle,
        activity=discord.Activity(type=discord.ActivityType.listening, name="Ta~ke take take take take take tatata~"))

    @commands.command()
    async def uptime(self, ctx):

        delta_uptime = datetime.utcnow() - self.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        day, hours = divmod(hours, 24)

        uptimeEmbed = discord.Embed(title="Uptime <:Hideri_Sleep:761132100979261460>", description=f"{hours}h, {minutes}m, {seconds}s", color=0x69ff96)
        uptimeEmbed.set_footer(text="WeebBot is currently on Heavy Maintenance!")

        await ctx.send(embed=uptimeEmbed)

    @commands.command()
    async def help(self, ctx):

        uptimeEmbed = discord.Embed(title="Lists of commands:", description="", color=0x69ff96)
        uptimeEmbed.add_field(name="Games:", value="> `roll`", inline=False)
        uptimeEmbed.add_field(name="Bot Info:", value="> `uptime` | `ping` | `version`", inline=False)
        uptimeEmbed.add_field(name="Moderation: (For Mods only!)", value="> `ban` | `kick` | `unban (not fully working)`", inline=True)
        uptimeEmbed.set_footer(text="The bot's prefix is '~'")

        await ctx.send(embed=uptimeEmbed)

    @commands.command()
    async def sys(self, ctx):

        sysEmbed = discord.Embed(title="System Information", description="", timestamp=datetime.utcnow(), color=0x69ff96)
        sysEmbed.add_field(name="CPU Usage:", value="> " + str(psutil.cpu_percent(interval=1)), inline=True)
        sysEmbed.add_field(name="Mem Usage:", value="> " + str(psutil.virtual_memory().percent), inline=True)     
        sysEmbed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)

        await ctx.send(embed=sysEmbed)

def setup(bot):
    bot.add_cog(System(bot))
