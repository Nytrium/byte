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
	async def _say(self, ctx, *, message):
		await ctx.send(f'> {ctx.author.mention} says {message}')
	#endregion

	#region quote command
	@commands.command(name='quote')
	async def _quote(self, ctx, user: discord.Member, *, message):
		await ctx.send(f'> {message}\n{user.mention}')
	#endregion

	#region 8ball command
	@commands.command(name='8ball')
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

		await ctx.send(f'> Q: {ctx.author}\n> A: {random.choice(answers)}')
	#endregion

	#region coinflip command
	@commands.command(name='coinflip')
	async def _coinflip(self, ctx):
		flip = random.randint(0,1)
		if flip:
			await ctx.send('It\'s heads!')
		else:
			await ctx.send('It\'s tails!')
	#endregion

	#region simp command
	@commands.command(name='simp')
	async def _simp(self, ctx, user: discord.Member):
		percent = random.randint(0, 100)
		await ctx.send(f'{user.mention} is {percent}% simp!')
	#endregion

	#region thot command
	@commands.command(name='thot')
	async def _thot(self, ctx, user: discord.Member):
		percent = random.randint(0, 100)
		await ctx.send(f'{user.mention} is {percent}% thot!')
	#endregion 
	
	#region ship command
	@commands.command(name='ship')
	async def _ship(self, ctx, user1: discord.Member, user2: discord.Member):
		if user1.id == '783272839435255818' or user2.id == '783272839435255818':
			await ctx.send(f'{user1.mention} and {user2.mention} are 0% shippable!\n<@783272839435255818> has a girlfriend, damn-it! >:(')
		else:
			percent = random.randint(0, 100)
			await ctx.send(f'{user1.mention} and {user2.mention} are {percent}% shippable!')
	#endregion

	#region hug command
	@commands.command(name='hug')
	async def _hug(self, ctx, user: discord.Member):
		await ctx.send(f'{ctx.author.mention} hugged {user.mention}! How cute!')
	#endregion

	#region slap command
	@commands.command(name='slap')
	async def _slap(self, ctx, user: discord.Member):
		await ctx.send(f'{ctx.author.mention} slapped {user.mention}! Ouch!')
	#endregion

	#region kiss command
	@commands.command(name='kiss')
	async def _kiss(self, ctx, user: discord.Member):
		await ctx.send(f'{ctx.author.mention} kissed {user.mention}! Awww')
	#endregion

	#region poke command
	@commands.command(name='poke')
	async def _poke(self, ctx, user: discord.Member):
		await ctx.send(f'{ctx.author.mention} poked {user.mention}!')
	#endregion

	#region suicide command
	@commands.command(name='suicide')
	async def _suicide(self, ctx):
		await ctx.author.kick(reason=None)
		await ctx.send(f'{ctx.author} commited suicide...\nwhat a sad death... :frowning:')
	#endregion

	#region sus command
	@commands.command(name='sus')
	async def _sus(self, ctx):
		await ctx.send('when the imposter is sus ඞ')
	#endregion
	

def setup(client):
	client.add_cog(Fun(client))
