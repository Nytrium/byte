import discord
from discord.ext import commands

class Moderation(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print('Moderation commands loaded.')
	
	@commands.command(name='kick')
	@commands.has_permissions(kick_members=True)
	async def _kick(self, ctx, user: discord.Member, *, reason=None):
		await user.kick(reason=reason)

	@commands.command(name='ban')
	@commands.has_permissions(ban_members=True)
	async def _ban(self, ctx, user: discord.Member, *, reason=None):
		await user.ban(reason=reason)
	
	@commands.command(name='clear')
	@commands.has_permissions(manage_messages=True)
	async def _clear(self, ctx, amount):
		pass

	@commands.command(name='user-info')
	@commands.has_permissions()
	async def _userinfo(self, ctx, user: discord.Member):
		embed=discord.Embed(title="User Info", description=user, color=0x5555ff)
		embed.set_thumbnail(url=user.avatar_url)
		embed.add_field(name="Username", value=f'{user.name}#{user.discriminator}', inline=True)
		embed.add_field(name="Joined Server At", value=str(user.joined_at)[:-10], inline=True)
		embed.add_field(name="Joined Discord At", value=str(user.created_at)[:-10], inline=False)
		embed.set_footer(text="Command run by " + str(ctx.author))
		await ctx.send(embed=embed)

	@commands.command(name='help')
	@commands.has_permissions()
	async def _help(self, ctx):
		embed=discord.Embed(title="Help", description="List of Commands", color=0x00ff00)
		embed.add_field(name="help", value="Bring up this embed.", inline=False)
		embed.add_field(name="say", value="Make the bot say something!", inline=False)
		embed.add_field(name="8ball", value="Say something and find out the possibilities of that happening!", inline=False)
		embed.add_field(name="user-info", value="Get some information about a specific user.", inline=False)
		
		await ctx.send(embed=embed)

def setup(client):
	client.add_cog(Moderation(client))