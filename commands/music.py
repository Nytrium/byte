import discord
from discord.ext import commands
from discord_slash import SlashCommand

guildIDs = [911595323363823676, 899316562014634075, 798236960677691432]

class Music:

	def __init__(self, client):
		self.client = client
	
	@commands.Cog.listener()
	async def on_ready(self):
		print('Music command loaded.')
	
	#region play command
	@SlashCommand(name='play', description='Play a song.', guild_ids=guildIDs)
	async def _play(self, ctx, *, song):
		if not ctx.voice_client:
			await ctx.invoke(self.client.get_cog('Voice')._join, ctx)
			
		if ctx.voice_client.is_playing():
			await ctx.voice_client.stop()
			
		await ctx.invoke(self.client.get_cog('Voice')._play, ctx, song)
		
		await ctx.send(f'Playing {song}')

	@_play.error
	async def _play_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send('You need to specify a song to play!')
		elif isinstance(error, commands.BadArgument):
			await ctx.send('That song doesn\'t exist!')
	#endregion

	#region skip command
	@SlashCommand(name='skip', description='Skip the current song.', guild_ids=guildIDs)
	async def _skip(self, ctx):
		if not ctx.voice_client:
			await ctx.invoke(self.client.get_cog('Voice')._join, ctx)
		
		if ctx.voice_client.is_playing():
			await ctx.voice_client.stop()
			
		await ctx.send('Skipped the current song!')
	
	@_skip.error
	async def _skip_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send('You don\'t have permissions to skip the song!')
	#endregion	

	#region stop command
	@SlashCommand(name='stop', description='Stop the music.', guild_ids=guildIDs)
	async def _stop(self, ctx):
		if not ctx.voice_client:
			await ctx.invoke(self.client.get_cog('Voice')._join, ctx)
		
		if ctx.voice_client.is_playing():
			await ctx.voice_client.stop()
			
		await ctx.send('Stopped the music!')
	
	@_stop.error
	async def _stop_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send('You don\'t have permission to stop the music!')
	#endregion
