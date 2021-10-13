import discord
from discord import Embed
from discord.ext import commands
from discord_slash import cog_ext
import random

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun commands loaded.')

    #region say command
    @cog_ext.cog_slash(name='say', description='Make the bot say something!', guild_ids=[897602500440498218])
    async def _say(self, ctx, *, message):
        await ctx.send(message)
    #endregion

    #region 8ball command
    @cog_ext.cog_slash(name='8ball', description='Ask a question and see the possibilities of it happening!', guild_ids=[897602500440498218])
    async def _8ball(self, ctx, *, question):
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
