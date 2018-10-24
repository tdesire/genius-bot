import discord
import lyricsgenius as genius
api = genius.Genius('I77pPvz_lAoG8k_9DJAol0bUOWQn0Xtngc1n2ytRE-J1oTeHKJfnIlPa3pZ3vTfp')
from discord.ext import commands
from discord.ext.commands import Bot
import config

TOKEN = config.TOKEN
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

client.run(TOKEN)