from util import default
import discord
from discord.ext import commands


class Slowmode(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.config = default.getJSON('config.json')
        self.running = False

    @commands.command(pass_context=True)
    async def slowmode(self, ctx, time=None):
            try:
                if time is not None: time = int(time.replace(' ', ''))
                if time is None or time <= 0:
                    await ctx.send(f'The syntax for **slowmode** command is: `{self.config.prefix}slowmode [time in seconds between messages]`')
                else:
                    if self.running is False:
                        ctx.channel.slowmode_delay = time
                        self.running = True
                        if time == 1:
                            await ctx.send(f'Slowmode successfully turned on with `{time}` second delay')
                        else:
                            await ctx.send(f'Slowmode successfully turned on with `{time}` seconds delay')
                    else:
                        #await ctx.channel.slowmode_delay: 0
                        self.running = False
                        await ctx.send('Slowmode successfully turned off')
            except ValueError:
                await ctx.send(f'That is not a number! `{self.config.prefix}slowmode [time in seconds between messages]`')


def setup(bot):
    bot.add_cog(Slowmode(bot))
