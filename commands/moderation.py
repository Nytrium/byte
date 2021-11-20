import discord
from discord.ext import commands
from discord_slash import cog_ext

guildIDs = [911595323363823676, 899316562014634075, 798236960677691432]

class Moderation(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print('Moderation commands loaded.')
	
	#region kick command
	@commands.has_permissions(kick_members=True)
	@cog_ext.cog_slash(name='kick', description='Kick a server member.', guild_ids=guildIDs)
	async def _kick(self, ctx, member: discord.Member, *, reason=None):
		if member == ctx.author:
			await ctx.send('You can\'t kick yourself!')
		else:
			await member.kick(reason=reason)
	#endregion

	#region ban command
	@commands.has_permissions(ban_members=True)
	@cog_ext.cog_slash(name='ban', description='Ban a server member.', guild_ids=guildIDs)
	async def _ban(self, ctx, member: discord.Member, *, reason=None):
		if member == ctx.author:
			await ctx.send('You can\'t ban yourself!')
		else:
			await member.ban(reason=reason)
	#endregion

	#region clear command
	@commands.has_permissions(manage_messages=True)
	@cog_ext.cog_slash(name='clear', description='Clear an amount of messages from the current channel.', guild_ids=guildIDs)
	async def _clear(self, ctx, amount=1):
		await ctx.channel.purge(limit=int(amount)+1)
		await ctx.send(f'Successfully deleted {amount} messages!', delete_after=2)
	#endregion

	#region nick command
	@commands.has_permissions(manage_nicknames=True)
	@cog_ext.cog_slash(name='nick', description='Give a server member a new nickname.', guild_ids=guildIDs)
	async def _nick(self, ctx, user: discord.Member, *, nickname):
		await user.edit(nick=nickname)
		await ctx.send('Successfully changed nickname for ' + str(user.mention))
	#endregion

	#region user-info command
	@commands.has_permissions()
	@cog_ext.cog_slash(name='user-info', description='Get information on a server member.', guild_ids=guildIDs)
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
	@commands.has_permissions()
	@cog_ext.cog_slash(name='help', description='Get a list of bot commands.', guild_ids=guildIDs)
	async def _help(self, ctx):
		embed=discord.Embed(title="Help", description="List of Commands", color=0x00ff00)
		embed.add_field(name="help", value="Bring up this embed.", inline=False)
		embed.add_field(name="say", value="Make the bot say something!", inline=False)
		embed.add_field(name="8ball", value="Say something and find out the possibilities of that happening!", inline=False)
		embed.add_field(name="thot", value="thot r8 machine", inline=False)
		embed.add_field(name="simp", value="simp r8 machine", inline=False)
		embed.add_field(name="coinflip", value="Flip a coin!", inline=False)
		embed.add_field(name="user-info", value="Get some information about a specific user.", inline=False)
		embed.add_field(name="clear", value="Clear a number of messages in a channel (default: 1)", inline=False)
		
		await ctx.send(embed=embed)
	#endregion

def setup(client):
	client.add_cog(Moderation(client))