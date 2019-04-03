from util import default
import asyncio
import discord
from discord.ext import commands


class Clear(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.config = default.getJSON('config.json')

    @commands.command(pass_context=True)
    async def clear(self, ctx, num=None):
        if num is None:
            await ctx.send(f'The syntax for **clear** command is: `{self.config.prefix}clear [number of messages to delete <= 1000]`')
        else:
            try:
                num = int(num)
                if num <= 1000:
                    await ctx.message.delete()
                    await ctx.channel.purge(limit=num)
                    type_message = 'message' if num == 1 else 'messages'
                    message = await ctx.send(f'Deleted `{num}` {type_message}!')
                    await asyncio.sleep(5)
                    await message.delete()
                else:
                    await ctx.send('Number of messages to delete must be <= 1000')

            except discord.Forbidden:
                message = await ctx.send("You don't have permission to execute this command.")
                await asyncio.sleep(5)
                await message.delete()

            except discord.HTTPException:
                message = await ctx.send("Deleting messages failed.")
                await asyncio.sleep(5)
                await message.delete()

            except ValueError:
                await ctx.send(f'That is not a number! `{self.config.prefix}clear [number of messages to delete <= 1000]`')


def setup(bot):
    bot.add_cog(Clear(bot))
