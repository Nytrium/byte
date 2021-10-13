import discord
from discord.ext import commands
from discord_slash import SlashCommand
import json
import os

with open('config.json', 'r') as f:
    CONFIG = json.load(f)
    TOKEN = CONFIG['TOKEN']
    prefix = CONFIG['prefix']

client = commands.Bot(command_prefix=prefix, help_command=None)
slash = SlashCommand(client, sync_commands=True)

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

client.run(TOKEN)
