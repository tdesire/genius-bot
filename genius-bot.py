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
    userID = message.author.id
    args = message.content.lower().replace("!lyricsfor", "").split("-")
    a = args[0]
    s = args[1]
    print(a)
    print(s)
    song = api.search_song(s, a).lyrics.split("\n")
    print(song)
    for line in song:
      if line == '':
        song.remove(line)
      else:
        await client.send_message(message.channel, "%s" % (line))

client.run(TOKEN)