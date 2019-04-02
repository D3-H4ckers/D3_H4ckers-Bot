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

    @commands.command(pass_context=True)
    async def about(self, ctx):
        await ctx.send(f'Name : {self.config.name}')
        await ctx.send(f'Developers : {self.config.developers}')

    @commands.command(pass_context=True)
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect(timeout=60.0, reconnect=True)
    
    @commands.command(pass_context=True)
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()
        
    @commands.command(pass_context=True)
    async def ping(self, ctx):
        await ctx.send(f'Pong')

    @commands.command(pass_context=True)
    async def coinflip(self, ctx):
        flip=random.randint(0,1)
        if flip==0:
            await ctx.send(f"Heads")
        if flip==1:
            await ctx.send(f"Tails")

    @commands.command(pass_context=True)
    async def name(self, ctx):
        await ctx.send(f'Your Name Is {ctx.message.author.name}!')

def setup(bot):
    bot.add_cog(Hello(bot))
