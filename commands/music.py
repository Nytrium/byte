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
	
	#region play command
	@cog_ext.cog_slash(name='play', description='Play a song.', guild_ids=guildIDs)
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
	@cog_ext.cog_slash(name='skip', description='Skip the current song.', guild_ids=guildIDs)
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
	@cog_ext.cog_slash(name='stop', description='Stop the music.', guild_ids=guildIDs)
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

	#region pause command
	@cog_ext.cog_slash(name='pause', description='Pause the music.', guild_ids=guildIDs)
	async def _pause(self, ctx):
		if not ctx.voice_client:
			await ctx.invoke(self.client.get_cog('Voice')._join, ctx)
		
		if ctx.voice_client.is_playing():
			ctx.voice_client.pause()
			
		await ctx.send('Paused the music!')
	
	@_pause.error
	async def _pause_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send('You don\'t have permission to pause the music!')
	#endregion

	#region resume command
	@cog_ext.cog_slash(name='resume', description='Resume the music.', guild_ids=guildIDs)
	async def _resume(self, ctx):
		if not ctx.voice_client:
			await ctx.invoke(self.client.get_cog('Voice')._join, ctx)
		
		if ctx.voice_client.is_paused():
			ctx.voice_client.resume()
			
		await ctx.send('Resumed the music!')

	@_resume.error
	async def _resume_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send('You don\'t have permission to resume the music!')
	#endregion

def setup(client):
	client.add_cog(Music(client))