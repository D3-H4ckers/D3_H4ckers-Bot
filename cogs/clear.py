from util import default
import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import Bot


class Clear(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.config = default.getJSON('config.json')


    @commands.command(pass_context=True)
    async def clear(self, ctx, num):
        try:
            num = int(num.replace(' ', ''))

            if isinstance(num, int):
                await ctx.message.delete()
                await ctx.channel.purge(limit=num)

                message = await ctx.send(f'Deleted `{num}` messages!')
                await asyncio.sleep(5)
                await message.delete()
            else:
                await ctx.send(f'The syntax for **clear** command is: `{self.config.prefix}clear [number of messages to delete]`')

        except discord.Forbidden:
            message = await ctx.send("You don't have permission to execute this command.")
            await asyncio.sleep(5)
            await message.delete()

        except discord.HTTPException:
            message = await ctx.send("Deleting messages failed.")
            await asyncio.sleep(5)
            await message.delete()

def setup(bot):
    bot.add_cog(Clear(bot))
