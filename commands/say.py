import discord
from discord.ext import commands

class Say(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='say')
    async def _say(self, ctx, *, msg):
        await ctx.send(msg)

def setup(client):
    client.add_cog(Say(client))
