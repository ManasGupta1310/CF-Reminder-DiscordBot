import os
import discord
import utils

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



@client.event
async def on_member_join(member):
    await member.channel.send(
        f'Hi {member.name}, Welcome to GhostXtrm server! I am a bot for reminding about the Contests!'
    )


@client.event
async def on_message(message):
    if message.author==client.user:
        return
    
    for guild in client.guilds:
        if guild.name==GUILD:
            break
    
    if message.content.startswith("$hello"):
        await message.channel.send(f"Hi {message.author}")
    
    if message.content.startswith("$contest"):
        utils.store_problems()
        contests=utils.get_problems()
        size=contests.shape
        if size[0]==0 or size[1]==0 :
            await message.channel.send("NO contests are going to be held for next 24 hours. Practice Hard until then!!")
        else:
            await message.channel.send("Contests are: ")
            for idx in contests.index:
                await message.channel.send(contests["Contest"][idx]+" "+contests["Link"][idx])


client.run(TOKEN)