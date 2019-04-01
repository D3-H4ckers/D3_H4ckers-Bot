author = """
        D3_H4ckers Bot
            Made by: D3_H4ckers
            Language: Python 3.6.7 on Ubuntu and Windows
"""

import discord
import json
import PyColored as c



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
    bot_info = loadJson('bot_info.json')

    print("\n")

    try:
        print(c.bold("--------------------------\n   Initializing the bot   \n--------------------------"))

        print("Initializing...", end='  |  ')
        client = discord.Client()
        client.run(bot_info['token'])

        print(c.brightgreen("Done!"))
    except:
        print(c.brightred("Failed!"))
        raise SystemError(c.brightred("Bot failed to initialize."))



def main():
    init()

if __name__ == "__main__":
    main()