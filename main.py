author = """
        D3_H4ckers Bot
            Made by: D3_H4ckers
            Language: Python 3.6.7 on Ubuntu and Windows
"""

import discord
import json
import PyColored as c
from .functions import sayhi

def loadJson(fileName):
    try:
        print(f"Loading {fileName}", end='  |  ')

        with open(fileName) as data:
            output = json.load(data)

        print(c.brightgreen("Done!"))
        return output
    except:
        print(c.brightred("Failed!"))
        raise SystemError(c.brightred(f"Illegal json file ({fileName})."))



def init():
    print(author)
    print(c.bold("-----------------------\n   Loading bot files   \n-----------------------"))
    global bot_info
    bot_info = loadJson('bot_info.json')

    print("\n")

    try:
        print(c.bold("--------------------------\n   Initializing the bot   \n--------------------------"))
        print("Initializing...")

        global client
        client = discord.Client()
    except:
        raise SystemError(c.brightred("Bot failed to initialize."))



init()

@client.event
async def on_ready():
    print(c.brightgreen("Bot successfully initialized!"))
    print("\nBot is running...")

@client.event
async def on_message(message):
    print(f"Message: {message.content}")
    if message.content.startswith(bot_info['prefix'] + 'sayhibitch'):
        sayhi(client, message.channel)

client.run(bot_info['token'])