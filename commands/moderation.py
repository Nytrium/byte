import discord
from discord.ext import commands

class Moderation(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print('Moderation commands loaded.')
	
	#region kick command
	@commands.has_permissions(kick_members=True)
	@commands.command(name='kick')
	async def _kick(self, ctx, member: discord.Member, *, reason=None):
		if member == ctx.author:
			await ctx.send('You can\'t kick yourself!', delete_after=3)
		else:
			await member.kick(reason=reason)
			await ctx.send(f'{member.mention} was kicked for {reason}.', delete_after=3)
   
	@_kick.error
	async def kick_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send('You don\'t have permission to kick members!', delete_after=3)
	#endregion

	#region ban command
	@commands.has_permissions(ban_members=True)
	@commands.command(name='ban')
	async def _ban(self, ctx, member: discord.Member, *, reason=None):
		if member == ctx.author:
			await ctx.send('You can\'t ban yourself!')
		else:
			await member.ban(reason=reason)
			await ctx.send(f'{member.mention} was banned for {reason}.', delete_after=3)

	@_ban.error
	async def ban_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send('You don\'t have permission to ban members!', delete_after=3)
	#endregion

	#region purge command
	@commands.has_permissions(manage_messages=True)
	@commands.command(name='clear')
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
	@commands.command(name='nick')
	async def _nick(self, ctx, user:discord.Member=discord.Message.author, *, nickname):
		await user.edit(nick=nickname)
		await ctx.send('Successfully changed nickname for ' + str(user.mention))

	@_nick.error
	async def nick_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send('You don\'t have permission to change nicknames!')
	#endregion

	#region user-info command
	@commands.has_permissions()
	@commands.command(name='user-info')
	async def _userinfo(self, ctx, user: discord.Member):
		embed=discord.Embed(title="User Info", description=user, color=0x5555ff)
		embed.set_thumbnail(url=user.avatar_url)
		embed.add_field(name="User ID", value=str(user.id), inline=True)
		embed.add_field(name="Joined Server At", value=str(user.joined_at)[:-10], inline=False)
		embed.add_field(name="Joined Discord At", value=str(user.created_at)[:-10], inline=False)
		embed.set_footer(text="Command run by " + str(ctx.author))
		await ctx.send(embed=embed)
	#endregion

	#region help command
	@commands.has_permissions()
	@commands.command(name='help')
	async def _help(self, ctx):
		embed=discord.Embed(title="Help", description="List of Commands", color=0x55ff55)
		embed.add_field(name="help", value="Bring up this embed.", inline=False)												# Help
		embed.add_field(name="say", value="Make the bot say something!", inline=False)											# Say
		embed.add_field(name="8ball", value="Say something and find out the possibilities of that happening!", inline=False)	# 8ball
		embed.add_field(name="thot", value="thot r8 machine", inline=False)														# Thot
		embed.add_field(name="simp", value="simp r8 machine", inline=False)														# Simp
		embed.add_field(name="kiss", value="kiss someone :kiss:", inline=False)													# Kiss
		embed.add_field(name="slap", value="slap someone lol", inline=False)													# Slap
		embed.add_field(name="poke", value="poke someone", inline=False)														# Poke
		embed.add_field(name="ship", value="Ship 2 people together, how cute!", inline=False)									# Ship
		embed.add_field(name="suicide", value="I don't think this needs an explanation", inline=False)							# Suicide
		embed.add_field(name="coinflip", value="Flip a coin!", inline=False)													# Coinflip
		embed.add_field(name="nick", value="Change a user's nickname.", inline=False)											# Nick
		embed.add_field(name="user-info", value="Get some information about a specific user.", inline=False)					# User-info
		embed.add_field(name="purge", value="Clear a number of messages in a channel.", inline=False)							# Purge
		embed.add_field(name="nuke", value="Nuke the channel.", inline=False)													# Nuke
		embed.add_field(name="kick", value="Kick a user from the server.", inline=False)										# Kick
		embed.add_field(name="ban", value="Ban a user from the server.", inline=False)											# Ban

		
		await ctx.send(embed=embed)
	#endregion
 
	#region mute command
	@commands.has_permissions(manage_roles=True)
	@commands.command(name='mute')
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
 
	#region nuke command
	@commands.has_permissions(manage_messages=True, manage_channels=True)
	@commands.command(name='nuke')
	async def _nuke(self, ctx, channel=discord.TextChannel):
		await channel.clone()
		await channel.delete()
		await ctx.send(f'Successfully nuked {channel.mention}.', delete_after=3)
	
	@_nuke.error
	async def nuke_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send('You don\'t have permission to purge messages!')
	#endregion

def setup(client):
	client.add_cog(Moderation(client))