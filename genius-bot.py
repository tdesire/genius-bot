import discord
import lyricsgenius as genius
import config
api = genius.Genius(config.GENIUS_TOKEN)
from discord.ext import commands
from discord.ext.commands import Bot
import random

TOKEN = config.BOT_TOKEN
Client = discord.Client()
client = commands.Bot(command_prefix = '!genius')
quiz = False
@client.event
async def on_ready():
  print('Bot is ready!')

@client.event
async def on_message(message):
  if message.content.upper() == ('!HI'):
    await client.send_message(message.channel, "What's up!")
  
  if message.content.upper() == '!HOW ARE YOU?':
    await client.send_message(message.channel, "I'm doing as well as a script feigning machine intelligence can be. How about you?")

  if message.content.upper() == '!WHAT ARE YOU?' or message.content.upper() == '!WHAT DO YOU DO?':
    await client.send_message(message.channel, "I'm a genius bot! You want some basic music info, I'm your bot. I can search up lyrics,  " +
    "download lyrics to your PC (if you're the host), and even give you some pretty basic info on specific songs.")
    await client.send_message(message.channel, "I'm powered by the LyricsGenius API wrapper, which scrapes song data from the Genius website via their web api. Pretty cool tech huh?")
    await client.send_message(message.channel, "Type !HELP for more instructions!")

  if message.content.upper() == "!HELP":
    await client.send_message(message.channel, "Here are some useful kewords: \n '!lyricsfor' [artist] - [song] *If I can find the song, I'll recite the lyrics*")
    await client.send_message(message.channel, "'!savelyricsfor' [artist] - [song] *If I can find the song, I'll download the lyrics to your computer as a txt file (must be bot host)*")
    await client.send_message(message.channel, "'!albumfor' [artist] - [song] *If I can find the song, I'll tell you the album it's featured on*")
    await client.send_message(message.channel, "'!releasedatefor' [artist] - [song] *If I can find the song, I'll tell you when the song was released*")
    await client.send_message(message.channel, "Notice the if clause. I'm not the smartest bot, so any typos or errors might screw up my search. I'm no Siri but I'm still kinda cool!")

  if message.content.upper().startswith('!LYRICSFOR'):
    args = message.content.lower().replace("!lyricsfor", "").split("-")
    a = args[0]
    s = args[1]
    song = api.search_song(s, a).lyrics.split("\n")
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

  # if message.content.upper().startswith('!QUIZMEON'):
  #   score = 0
  #   a = message.content.lower().replace('!quizmeon', "")
  #   await client.send_message(message.channel, "Retrieving data on {} . I'm going to quiz on you on the first batch of songs I can find...".format(a))
  #   artist = api.search_artist(a, max_songs=50)
  #   await client.send_message(message.channel, "generating questions...")
  #   for q in range(10):
  #     song = artist.songs[random.randint(1,artist.num_songs)]
  #     song_name = song.title
  #     song_list = song.lyrics.split('\n')
  #     vol = len(song_list)
  #     line = song_list[random.randint(1, vol)]
  #     await client.send_message(message.channel, "{}.  What song is this lyric from? ---\n  {}".format(q, line))
  #     if message.content.upper() == song_name.upper():
  #       score += 1
  #       await client.send_message(message.channel, "Correct! You now have  '{}'  points!".format(score))
  #     else:
  #       await client.send_message(message.channel, "Sorry, the correct answer is  '{}' . You currently have  '{}'  points.".format(song_name, score))
  #   if score == 10:
  #     await client.send_message(message.channel, "Wow, you're definitely a fan! Congrats, you got a perfect score!")
  #   elif score >= 7:
  #     await client.send_message(message.channel, "Impressive! You sure are a  {}  stan lol".format(a))
  #   elif score < 5:
  #     await client.send_message(message.channel, "Hmm. You must be new to this artist. Might want to go study their catalogue")
  #   else:
  #     await client.send_message(message.channel, "Not bad, but you could've done better. You must be a casual fan")
client.run(TOKEN)