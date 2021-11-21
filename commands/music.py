import discord
from discord.ext import commands
from discord_slash import cog_ext

guildIDs = [911595323363823676, 899316562014634075, 798236960677691432]

class Music(commands.Cog):

	def __init__(self, client):
		self.client = client
	
	@commands.Cog.listener()
	async def on_ready(self):
		print('Music command loaded.')
	
	#region connect command
	@cog_ext.cog_slash(name='connect', description='Connect to a voice channel.', guild_ids=guildIDs)
	async def _connect(self, ctx, channel: discord.VoiceChannel):
		await channel.connect()
		await ctx.send(f'Connected to {channel.name}.')
	#endregion

	#region play command
	@cog_ext.cog_slash(name='play', description='Play a song.', guild_ids=guildIDs)
	async def _play(self, ctx, *, song):
		await discord.VoiceClient.play(discord.FFmpegPCMAudio(song), after=lambda e: print('Player error: %s' % e) if e else None)
		await ctx.send('Playing ' + song)
		await ctx.voice_client.disconnect()
		await ctx.send('Disconnected from voice channel.')
	#endregion

	#region stop command
	@cog_ext.cog_slash(name='stop', description='Stop the current song.', guild_ids=guildIDs)
	async def _stop(self, ctx):
		if ctx.voice_client is None:
			await ctx.send('I am not playing anything.')
			return
		await ctx.voice_client.disconnect()
		await ctx.send('Stopped playing.')
	#endregion

def setup(client):
	client.add_cog(Music(client))

