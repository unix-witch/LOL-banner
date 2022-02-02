#https://discord.com/api/oauth2/authorize?client_id=937810355206357062&permissions=8&scope=bot

import os 
import random
import discord
from discord.ext import commands
from keepalive import keepAlive


intents = discord.Intents.all()
intents.members = True



client = commands.Bot(command_prefix='!', intents=intents)

messages = [
    "Stop playing league of legends",
    "Take a shower",
    "Among us??? Sussy??? Imposter league of legends?"
]



@client.event
async def on_ready():
    print("Ready!")
    print(client.guilds)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} sussy bakers"))
    members = 0
    
    for guild in client.guilds:
        for member in guild.members:
            members += 1

    with open("members.txt", "w") as f:
        f.write(str(members))




@client.event
async def on_member_update(before, after):
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=random.choice(status)))


    if after.activity != None:
        print(after.name)
        if len(after.activities) > 1:
            print(after.activities[1].name)
            if str(after.activities[1].name).lower() == "league of legends":
                print("banning")
                try:
                    with open("hall-of-shame.txt", "a+") as f:
                        f.write(after.name)


                    await after.send(random.choice(messages))
                    await after.ban(reason='Playing League of legends')
                except discord.errors.Forbidden:
                    print("Not valid permissions")
                    after.send("")

                print(after.activities[1])





keepAlive()
client.run(os.environ['TOKEN']) 
