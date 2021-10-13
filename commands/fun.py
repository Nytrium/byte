import discord
from discord.ext import commands
import random

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun commands loaded.')

    #region say command
    @commands.command(name='say')
    async def _say(self, ctx, *, msg):
        await ctx.send(msg)
    #endregion

    #region 8ball command
    @commands.command(name='8ball')
    async def _8ball(self, ctx, *, args):
        answers = [
                'It is certain.',
                'It is decidedly so.',
                'Without a doubt.',
                'Yes, definitely.',
                'You may rely on it.',
                'As I see it, yes.',
                'Most likely.',
                'Outlook good.',
                'Yes.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate anf ask again.',
                "Don't count on it.",
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Very doubtful.'
                ]

        await ctx.send(random.choice(answers))
    #endregion
    
def setup(client):
    client.add_cog(Fun(client))
