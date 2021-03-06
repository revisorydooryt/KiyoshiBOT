import discord
from discord.ext import commands
import sys
import traceback
import os
from dotenv import load_dotenv

# This will keep bot alive
from keep_alive import keep_alive

bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'))
bot.remove_command('help')

initial_extensions = ['cogs.Games','cogs.Version', 'cogs.System', 'cogs.Moderation', 'cogs.nhentai']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}', file=sys.stderr)
            traceback.print_exc()
           
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

keep_alive()
bot.run(TOKEN)
