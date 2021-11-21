import discord
from discord.ext import commands
from discord_slash import cog_ext
import youtube_dl

guildIDs = [911595323363823676, 899316562014634075, 798236960677691432]

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
		await ctx.send(f'Searching for {song}...')
		
		ydl_opts = {
			'format': 'bestaudio/best',
			'quiet': True,
			'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'mp3',
				'preferredquality': '192',
			}],
		}
		
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			info = ydl.extract_info(f'ytsearch:{song}', download=False)
		
		if 'entries' in info:
			info = info['entries'][0]
		
		url = info['url']
		
		if not ctx.voice_client:
			await ctx.author.voice.channel.connect()
			await ctx.send(f'Connected to {ctx.author.voice.channel.name}.')
		
		player = discord.FFmpegPCMAudio(url)
		player.start()
		
		await ctx.send(f'Playing {info["title"]}.')
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

