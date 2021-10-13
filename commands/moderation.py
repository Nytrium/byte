import discord
from discord.ext import commands
from discord.ext.commands.errors import MissingPermissions

class Moderation(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print('Moderation commands loaded.')
	
	#region kick command
	@commands.command(name='kick')
	@commands.has_permissions(kick_members=True)
	async def _kick(self, ctx, user: discord.Member, *, reason=None):
		await user.kick(reason=reason)
	#endregion

	#region ban command
	@commands.command(name='ban')
	@commands.has_permissions(ban_members=True)
	async def _ban(self, ctx, user: discord.Member, *, reason=None):
		await user.ban(reason=reason)
	#endregion

	#region clear command
	@commands.command(name='clear')
	@commands.has_permissions(manage_messages=True)
	async def _clear(self, ctx, amount=1):
		await ctx.channel.purge(limit=amount+1)
		await ctx.send(f'Successfully deleted {amount} messages!', delete_after=2)
	#endregion

	#region nick command
	@commands.command(name='nick')
	@commands.has_permissions(manage_nicknames=True)
	async def _nick(self, ctx, user: discord.Member, *, nickname=None):
		await user.edit(nick=nickname)
		await ctx.send('Successfully changed nickname for ' + str(user.mention))
	#endregion

	#region user-info command
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
	#endregion

	#region help command
	@commands.command(name='help')
	@commands.has_permissions()
	async def _help(self, ctx):
		embed=discord.Embed(title="Help", description="List of Commands", color=0x00ff00)
		embed.add_field(name="help", value="Bring up this embed.", inline=False)
		embed.add_field(name="say", value="Make the bot say something!", inline=False)
		embed.add_field(name="8ball", value="Say something and find out the possibilities of that happening!", inline=False)
		embed.add_field(name="user-info", value="Get some information about a specific user.", inline=False)
		embed.add_field(name="clear", value="Clear a number of messages in a channel (default: 1)", inline=False)
		
		await ctx.send(embed=embed)
	#endregion

def setup(client):
	client.add_cog(Moderation(client))