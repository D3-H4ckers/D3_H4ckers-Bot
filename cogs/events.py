import discord
import PyColored as c
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(c.brightgreen('Bot successfully initialized!'))
        await bot.change_presence(status=discord.Status.online)


def setup(bot):
    bot.add_cog(Events(bot))
