import discord
from util import default
from discord.ext import commands


class Hello(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.config = default.getJSON('config.json')

    @commands.command(pass_context=True)
    async def hi(self, ctx):
        await ctx.send(f'Hello {ctx.message.author.name}!')

    @commands.command()
    async def about(self, ctx):
        await ctx.send(f'Name : {self.config.name}')
        await ctx.send(f'Developers : {self.config.developers}')


def setup(bot):
    bot.add_cog(Hello(bot))
