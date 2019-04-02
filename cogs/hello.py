import discord
from util import default
from discord.ext import commands


class Hello(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.config = default.getJSON('config.json')

    @commands.command(pass_context=True)
    async def hi(self, ctx):
        await bot.say(f'Hello {ctx.message.author.name}!')

    @commands.command()
    async def about(self):
        await bot.say(f'Name : {self.config.name}')
        await bot.say(f'Developers : {self.config.developers}')


def setup(bot):
    bot.add_cog(Hello(bot))
