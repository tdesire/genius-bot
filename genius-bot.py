import discord
import lyricsgenius as genius
import config
api = genius.Genius(config.GENIUS_TOKEN)
from discord.ext import commands
from discord.ext.commands import Bot
import config

TOKEN = config.BOT_TOKEN
Client = discord.Client()
client = commands.Bot(command_prefix = '!genius')

@client.event
async def on_ready():
  print('Bot is ready!')

@client.event
async def on_message(message):
  if message.content.upper().startswith('!LYRICSFOR'):
    args = message.content.lower().replace("!lyricsfor", "").split("-")
    a = args[0]
    s = args[1]
    song = api.search_song(s, a).lyrics.split("\n")
    print(song)
    for line in song:
      if line == '':
        song.remove(line)
      else:
        await client.send_message(message.channel, "%s" % (line))
  
  if message.content.upper().startswith('!SAVELYRICSFOR'):
    args = message.content.lower().replace("!savelyricsfor", "").split("-")
    a = args[0]
    s = args[1]
    await client.send_message(message.channel, "Downloading the lyrics for  '{}'  by  '{}'  to the bot's host computer...".format(s, a))
    song_to_save = api.search_song(s, a)
    song_to_save.save_lyrics(format_='txt')

    await client.send_message(message.channel, "Here is a snippet of the lyrics you've requested: ")
    song_to_save_list = api.search_song(s, a).lyrics.split("\n")
    snippet = song_to_save_list[1:8]

    for line in snippet:
      if line == '':
        snippet.remove(line)
      else:
        await client.send_message(message.channel, "%s" % (line))

  if message.content.upper().startswith('!ALBUMFOR'):
    args = message.content.lower().replace('!albumfor', "").split('-')
    a = args[0]
    s = args[1]
    await client.send_message(message.channel, "Finding the album for  '{}'  by  '{}' ...".format(s, a))
    album = api.search_song(s, a).album
    await client.send_message(message.channel, "'{}'  is featured on the album  '{}'  by  '{}'".format(s, album, a))

  if message.content.upper().startswith('!RELEASEDATEFOR'):
    args = message.content.lower().replace('!releasedatefor', "").split('-')
    a = args[0]
    s = args[1]
    await client.send_message(message.channel, "Finding the release date for the track  '{}'  by  '{}' ...".format(s, a))
    release_date = api.search_song(s, a).year
    await client.send_message(message.channel, "Release date for  '{}'  by  '{}' :  '{}'".format(s, a, release_date))


client.run(TOKEN)