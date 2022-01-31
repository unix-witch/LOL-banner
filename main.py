import os 
import discord
from discord.ext import commands
from keepalive import keepAlive


intents = discord.Intents.all()
intents.members = True



client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print("Ready!")


@client.event
async def on_member_update(before, after):

    if after.activity != None:
        print(len(after.activities))
        if len(after.activities) > 1:
            if str(after.activities[1]).lower() == "league of legends":
                print("banning")
                try:
                    await after.ban()
                except discord.errors.Forbidden:
                    print("Not valid permissions")

                print(after.activities[1])





keepAlive()
client.run(os.environ['TOKEN'])
