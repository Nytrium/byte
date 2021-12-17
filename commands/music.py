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
		# start playing a song in the current voice channel using youtube_dl
		# if the user is in a voice channel, connect to the voice channel
		if ctx.author.voice:
			await ctx.author.voice.channel.connect()
		# if the user is not in a voice channel, send an error message
		else:
			await ctx.send('You are not in a voice channel.')
			return

		# create a ytdl object
		ytdl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
		# get the info of the song
		info = ytdl.extract_info(song, download=False)
		# get the url of the song
		url = info['url']
		# get the title of the song
		title = info['title']
		# get the duration of the song
		duration = info['duration']
		
		# play the song in the voice channel and send a message
		player = await ctx.author.voice.channel.connect()
		player.play(discord.FFmpegPCMAudio(url))
		await ctx.send(f'Now playing: {title}\nSong Length: {duration}')
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

def setup(client):
	client.add_cog(Music(client))
