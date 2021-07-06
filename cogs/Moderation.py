import discord
from discord.ext import commands
from discord.ext.commands.core import command

class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #kick cmd
    @commands.command(name='kick', pass_context = True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, context, member: discord.Member):
        
        await member.kick()
        await context.send('User '+ member.display_name + ' has been kicked.')

    #ban cmd
    @commands.command(name='ban', pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def ban(self, context, member: discord.Member, *, reason=None):

        await member.ban(reason=reason)
        await context.send('User '+ member.display_name + ' has been banned.')

    #unban cmd
    @commands.command(name='unban', pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def unban(self, context, member: discord.Member, *, reason=None):

        await member.unban(reason=reason)
        await context.send('User '+ member.display_name + ' has been unbanned.')

def setup(bot):
    bot.add_cog(Moderation(bot))