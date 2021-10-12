import discord
import json
import os
from discord.ext import commands

with open('config.json', 'r') as f:
    CONFIG = json.load(f)
    TOKEN = CONFIG['TOKEN']
    prefix = CONFIG['prefix']

client = commands.Bot(command_prefix=prefix, help_command=None)

@client.command()
async def on_ready():
    print('Bot ready.')

@client.command(name='load')
async def _load(ctx, extension):
    client.load_extension(f'commands.{extension}')

@client.command(name='unload')
async def _unload(ctx, extension):
    client.unload_extension(f'commands.{extension}')

for fileName in os.listdir('./commands'):
    if fileName.endswith('.py'):
        client.load_extension(f'commands.{fileName[:-3]}')

client.run(TOKEN)
