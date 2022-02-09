from http import client
from multiprocessing.connection import Client
import discord

client=Client(__name__)

@client.event
async def on_startup():
    print("We are online now!")