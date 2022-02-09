from ast import Break
import os
import discord

from dotenv import load_dotenv

load_dotenv()

TOKEN=os.getenv('DISCORD_TOKEN')
GUILD=os.getenv('DISCORD_SERVER')

client=discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name==GUILD:
            break

    print("We are online now!")
    print(f"Connected to the server: {guild.name}: {guild.id}")

client.run(TOKEN)