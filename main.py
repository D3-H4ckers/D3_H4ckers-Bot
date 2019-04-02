import json
import discord
import PyColored as c
from discord.ext import commands
from collections import namedtuple


def getJSON(file: str) -> json:
    try:
        print(c.bold("-----------------------\n   Loading bot files   \n-----------------------"))
        return json.load(open(file), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    except FileNotFoundError:
        raise FileNotFoundError(c.brightred(f'{file} file was not found.'))

config = getJSON('config.json')
bot = commands.Bot(command_prefix=config.prefix, status=discord.Status.idle)
bot.remove_command('help')


@bot.event
async def on_ready():
    print(c.brightgreen('Bot successfully initialized!'))
    await bot.change_presence(status=discord.Status.online)


@bot.command(pass_context=True)
async def hi(ctx):
    await bot.say(f'Hello {ctx.message.author.name}!')


@bot.command()
async def about():
    await bot.say(f'Name : {config.name}')
    await bot.say(f'Developers : {config.developers}')

try:
    bot.run(config.token)
except:
    raise SystemError(c.brightred('Bot failed to be initialized.'))
