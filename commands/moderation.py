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
   
	@_kick.error
	async def kick_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send('You don\'t have permission to kick members!')
	#endregion

	#region ban command
	@commands.has_permissions(ban_members=True)
	@cog_ext.cog_slash(name='ban', description='Ban a server member.', guild_ids=guildIDs)
	async def _ban(self, ctx, member: discord.Member, *, reason=None):
		if member == ctx.author:
			await ctx.send('You can\'t ban yourself!')
		else:
			await member.ban(reason=reason)

	@_ban.error
	async def ban_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send('You don\'t have permission to ban members!')
	#endregion

	#region purge command
	@commands.has_permissions(manage_messages=True)
	@cog_ext.cog_slash(name='clear', description='Clear an amount of messages from the current channel.', guild_ids=guildIDs)
	async def _purge(self, ctx, amount=1):
		await ctx.channel.purge(limit=int(amount)+1)
		await ctx.send(f'Successfully purged {amount} messages!', delete_after=2)

	@_purge.error
	async def purge_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send('You don\'t have permission to clear messages!')
	#endregion

	#region nick command
	@commands.has_permissions(manage_nicknames=True)
	@cog_ext.cog_slash(name='nick', description='Give a server member a new nickname.', guild_ids=guildIDs)
	async def _nick(self, ctx, user: discord.Member, *, nickname):
		await user.edit(nick=nickname)
		await ctx.send('Successfully changed nickname for ' + str(user.mention))

	@_nick.error
	async def nick_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send('You don\'t have permission to change nicknames!')
	#endregion

	#region user-info command
	@commands.has_permissions()
	@cog_ext.cog_slash(name='user-info', description='Get information on a server member.', guild_ids=guildIDs)
	async def _userinfo(self, ctx, user: discord.Member):
		embed=discord.Embed(title="User Info", description=user, color=0x5555ff)
		embed.set_thumbnail(url=user.avatar_url)
		embed.add_field(name="Username", value=f'{user.name}#{user.discriminator}', inline=True)
		embed.add_field(name="Joined Server At", value=str(user.joined_at)[:-10], inline=True)
		embed.add_field(name="Joined Discord At", value=str(user.created_at)[:-10], inline=True)
		if ctx.author.id == 792162727907950652:
			embed.add_field(name="Height", value="short", inline=False)
		elif ctx.author.id == 711179491132571689:
			embed.add_field(name="Height", value="Luigi", inline=False)
		else:
			pass
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
 
	#region mute command
	@commands.has_permissions(manage_roles=True)
	@cog_ext.cog_slash(name='mute', description='Mute a server member.', guild_ids=guildIDs)
	async def _mute(self, ctx, member: discord.Member):
		if member == ctx.author:
			await ctx.send('You can\'t mute yourself!')
		else:
			role = discord.utils.get(ctx.guild.roles, name='Muted')
			await member.add_roles(role)
			await ctx.send('Successfully muted ' + str(member.mention))
   
	@_mute.error
	async def mute_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send('You don\'t have permission to mute members!')
	#endregion
 
	#region unmute command
	@commands.has_permissions(manage_roles=True)
	@cog_ext.cog_slash(name='unmute', description='Unmute a server member.', guild_ids=guildIDs)
	async def _unmute(self, ctx, member: discord.Member):
		if member == ctx.author:
			await ctx.send('You can\'t unmute yourself!')
		else:
			role = discord.utils.get(ctx.guild.roles, name='Muted')
			await member.remove_roles(role)
			await ctx.send('Successfully unmuted ' + str(member.mention))
   
	@_unmute.error
	async def unmute_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send('You don\'t have permission to unmute members!')
	#endregion
 
	#region nuke command
	@commands.has_permissions(manage_messages=True, manage_channels=True)
	@cog_ext.cog_slash(name='nuke', description='Purge a whole channel worth of messages.', guild_ids=guildIDs)
	async def _nuke(self, ctx, channel=discord.TextChannel):
		channel.clone()
		channel.delete()
	
	@_nuke.error
	async def nuke_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send('You don\'t have permission to purge messages!')
	#endregion

def setup(client):
	client.add_cog(Moderation(client))