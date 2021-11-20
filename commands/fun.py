import discord
from discord import message
from discord.ext import commands
from discord_slash import cog_ext
import random

guildIDs = [911595323363823676, 899316562014634075, 798236960677691432]

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun commands loaded.')

    #region say command
    @cog_ext.cog_slash(name='say', description='Make the bot say something!', guild_ids=guildIDs)
    async def _say(self, ctx, *, message):
        await ctx.send(f'> {ctx.author.mention} says {message}')
    #endregion

    #region 8ball command
    @cog_ext.cog_slash(name='8ball', description='Ask a question and see the possibilities of it happening!', guild_ids=guildIDs)
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

    #region coinflip command
    @cog_ext.cog_slash(name='coinflip', description='Flip a coin!', guild_ids=guildIDs)
    async def _coinflip(self, ctx):
        flip = random.randint(0,1)
        if flip:
            await ctx.send('It\'s heads!')
        else:
            await ctx.send('It\'s tails!')
    #endregion

    #region simp command
    @cog_ext.cog_slash(name='simp', description='simp r8 machine', guild_ids=guildIDs)
    async def _simp(self, ctx, user: discord.Member):
        percent = random.randint(0, 100)
        await ctx.send(f'{user.mention} is {percent}% simp!')
    #endregion

    #region thot command
    @cog_ext.cog_slash(name='thot', description='thotties do be thotting', guild_ids=guildIDs)
    async def _thot(self, ctx, user: discord.Member):
        percent = random.randint(0, 100)
        await ctx.send(f'{user.mention} is {percent}% thot!')
    #endregion 
    
    #region ship command
    @cog_ext.cog_slash(name='ship', description='ship two people together', guild_ids=guildIDs)
    async def _ship(self, ctx, user1: discord.Member, user2: discord.Member):
        percent = random.randint(0, 100)
        name1 = user1.display_name.split()
        name2 = user2.display_name.split()
        
        joinednames = name1 + name2
        await ctx.send(f'{user1.mention} and {user2.mention} are {percent}% shippable!\nThey are {joinednames}!')

    #endregion

def setup(client):
    client.add_cog(Fun(client))
