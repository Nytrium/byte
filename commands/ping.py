import discord
from discord.ext import commands

class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='ping')
    async def _ping(self, ctx):
        await ctx.send('Pong! :ping_pong:')

def setup(client):
    client.add_cog(Ping(client))
