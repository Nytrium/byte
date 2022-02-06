import os

import discord  # pip install discord.py
from discord.ext import commands  # pip install discord.py
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix='$', help_command=None, intents=discord.Intents.all())


@client.event
async def on_ready():
    print('Bot is ready!')


@client.command(name='load')
async def _load(extension):
    client.load_extension(f'commands.{extension}')


@client.command(name='unload')
async def _unload(extension):
    client.unload_extension(f'commands.{extension}')


@client.command(name='reload')
async def _reload(extension):
    client.unload_extension(f'commands.{extension}')
    client.load_extension(f'commands.{extension}')


for fileName in os.listdir('./commands'):
    if fileName.endswith('.py'):
        client.load_extension(f'commands.{fileName[:-3]}')

client.run(os.environ['TOKEN'])
