from asyncio import tasks
import os
import discord
import utils
from discord.ext import commands, tasks
import random

TOKEN=os.environ['DISCORD_TOKEN']
GUILD=os.environ['DISCORD_SERVER']

intents = discord.Intents.all()
client=discord.Client(intents=intents)

bot=commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name==GUILD:
            break

    print("We are online now!")
    print(f"Connected to the server: {guild.name}: {guild.id}")



@client.event
async def on_member_join(member):
    name="general"
    id=0
    for channel in client.get_all_channels():
        if channel.name==name:
            id=channel.id

    channel=client.get_channel(id)
    await channel.send(
        f'Hi @{member.name}, Welcome to GhostXtrm server! I am a bot for reminding about the Contests and giving problems to solve!'
    )
    print("Sent Join Message")

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
        utils.store_contest()
        contests=utils.get_contest()
        size=contests.shape
        if size[0]==0 or size[1]==0 :
            await message.channel.send("NO contests are going to be held for next 24 hours. Practice Hard until then!!")
        else:
            await message.channel.send("Contests are: ")
            for idx in contests.index:
                await message.channel.send(contests["Contest"][idx]+" "+contests["Link"][idx])
    
    if message.content.startswith("$problem"):
        arr=message.content.split(" ")
        if len(arr)==1:
            x=4000
            y=0
        elif len(arr)==2:
            x=arr[1]
            y=0
        else:
            x=arr[1]
            y=arr[2]
        
        utils.store_problems(x,y)
        problems=utils.get_problems()
        size=problems.shape
        if size[0]==0 or size[1]==0 :
            await message.channel.send("No such problems found!")
        else:
            await message.channel.send("the Three problems are: ")
            rand=random.sample(range(0,size[0]),3)    
            for idx in rand:
                await message.channel.send(problems["Name"][idx]+" "+problems["Link"][idx])


@bot.command(name="hello")
async def on_message(message):
    await message.channel.send(f"Hi {message.author}")

@tasks.loop(minutes=1)
async def called_once_a_day():
    print("1 minute passed")

client.run(TOKEN)
