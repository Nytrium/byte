import discord
from discord.ext import commands
from discord_slash import cog_ext
import youtube_dl
import ffmpeg

guildIDs = [911595323363823676, 899316562014634075, 798236960677691432, 918424005696958484]

class Music(commands.Cog):

	def __init__(self, client):
		self.client = client
	
	@commands.Cog.listener()
	async def on_ready(self):
		print('Music command loaded.')
	
	#region connect command
	@cog_ext.cog_slash(name='connect', description='Connect to a voice channel.', guild_ids=guildIDs)
	async def _connect(self, ctx):
		await ctx.author.voice.channel.connect()
		await ctx.send(f'Connected to {ctx.author.voice.channel.name}.')
	#endregion

	#region play command
	@cog_ext.cog_slash(name='play', description='Play a song.', guild_ids=guildIDs)
	async def _play(self, ctx, *, song):
		# check if the user is in a voice channel, if not, return an error message
		if not ctx.author.voice or not ctx.author.voice.channel:
			await ctx.send('You are not in a voice channel.')
			return

		# check if the user is in a voice channel and if the bot isn't already connected to the voice channel, connect
		if not ctx.voice_client or not ctx.voice_client.is_connected():
			await ctx.author.voice.channel.connect()

		# print information about the song to the chat and play the song using youtube_dl
		ydl_opts = {
			'format': 'bestaudio/best',
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'mp3',
				'preferredquality': '192'
			}]
		}
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			info = ydl.extract_info(song, download=False)
			await ctx.send(f'Now playing: {info["title"]}')
			source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(info['url']))
			ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)

		# disconnect from the voice channel if the song is finished playing
		ctx.voice_client.stop()
		await ctx.voice_client.disconnect()
		
	#endregion

	#region disconnect command
	@cog_ext.cog_slash(name='disconnect', description='Disconnect from the voice channel.', guild_ids=guildIDs)
	async def _disconnect(self, ctx):
		if ctx.voice_client:
			await ctx.voice_client.disconnect()
			await ctx.send(f'Disconnected from {ctx.author.voice.channel.name}.')
		else:
			await ctx.send('I am not connected to a voice channel.')
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

	#region leave command
	@cog_ext.cog_slash(name='leave', description='Leave the voice channel.', guild_ids=guildIDs)
	async def _leave(self, ctx):
		if ctx.voice_client is None:
			await ctx.send('I am not connected to a voice channel.')
			return
		await ctx.voice_client.disconnect()
		await ctx.send('Left the voice channel.')
	#endregion

def setup(client):
	client.add_cog(Music(client))
