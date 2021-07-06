import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot
from hentai import Utils, Sort, Option, Hentai, Format, Tag, Option

class nhentai(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gcode(self, ctx):

        doujin = Hentai(Utils.get_random_id())

        hentaiEmbed = discord.Embed(title="Code Generated! <a:pepe:789701805801472050>", description="", color=0x69ff96)
        hentaiEmbed.add_field(name="Title:", value=(doujin), inline=False)
        hentaiEmbed.add_field(name="Code", value=(doujin.id), inline=False)
        hentaiEmbed.add_field(name="Tags", value=([tag.name for tag in doujin.tag]))
        hentaiEmbed.set_image(url=(doujin.cover))
        hentaiEmbed.set_footer(text="WeebBot is currently on Heavy Maintenance!")

        await ctx.message.channel.send(embed=hentaiEmbed)



#search = hentai.search(query)
#print (search)

        for doujin in Utils.search_by_query('tag:yaoi -tomgirl', sort=Sort.PopularWeek):

            yaoiEmbed = discord.Embed(title="Title: <a:pepe:789701805801472050>", description=(doujin.title(Format.Pretty)), color=0x69ff96)
            yaoiEmbed.add_field(name="Code", value=(doujin.id), inline=False)
            yaoiEmbed.add_field(name="Tags", value=("obviously yaoi...?"))
            yaoiEmbed.set_image(url=(doujin.cover))

            await ctx.message.channel.send(embed=yaoiEmbed)
        footerembed=discord.Embed()
        footerembed.set_footer(text="nhentai.net", icon_url="https://cdn.discordapp.com/emojis/799969346813296680.png?v=1")
        await ctx.message.channel.send(embed=footerembed)

def setup(bot):
    bot.add_cog(nhentai(bot))