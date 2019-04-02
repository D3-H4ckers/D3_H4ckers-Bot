import os
import discord
import PyColored as c
from util import default
from discord.ext import commands

config = default.getJSON('config.json')
bot = commands.Bot(command_prefix=config.prefix, status=discord.Status.idle)

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")

bot.remove_command('help')

try:
    bot.run(config.token)
except:
    raise SystemError(c.brightred('Bot failed to be initialized.'))
