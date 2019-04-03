import discord
import random
import youtube_dl
from util import default
from discord.ext import commands

class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.config = default.getJSON('config.json')

    players = {}
    client = commands.Bot(command_prefix= '!')

    @commands.command(pass_context=True)
    async def play(self,ctx, url):
        server = ctx.message.author.server
        voice_client = client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url)
        players[server.id] = player
        player.start()

def setup(bot):
    bot.add_cog(Music(bot))
