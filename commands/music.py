import discord
from discord.ext import commands
from discord_slash import cog_ext
import youtube_dl
import ffmpeg

guildIDs = [798236960677691432, 918424005696958484, 899316562014634075, 922998853827964978]

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

		# create a ytdl object
		ytdl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

		# check if the song is a url or a search term
		if 'www.youtube.com' in song or 'youtube.com' in song:
			# if the song is a url, use the url
			info = ytdl.extract_info(song, download=False)
			song = info['url']
		else:
			# if the song is a search term, use the search term
			info = ytdl.extract_info(f'ytsearch:{song}', download=False)
			song = info['entries'][0]['url']
		
		# download and play the song using the information and youtube_dl
		player = await ctx.voice_client.create_ytdl_player(song)
		player.start()
		await ctx.send(f'Now playing {player.title}.')
		
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
