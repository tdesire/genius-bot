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
    userID = message.author.id
    if message.content.find("-") == -1:
      await client.send_message(message.channel, "Sorry <@%s>, the song search must follow the [artist] - [song] structure. Type *!help* for more details. " % (userID))
    else: 
      args = message.content.lower().replace("!lyricsfor", "").split("-")
      a = args[0]
      s = args[1]
      await client.send_message(message.channel, "Searching for the lyrics to  *{}*  by  *{}* ...".format(s, a))
      song = api.search_song(s, a)
      if song:
        url = song.url
        lyrics = song.lyrics.split("\n")
        for line in lyrics:
          if line == '':
            lyrics.remove(line)
          else:
            await client.send_message(message.channel, "*{}*".format(line))
        await client.send_message(message.channel, "If you'd like to download the lyrics as a txt file, enter '!savelyricsfor' [artist] - [song]")
        await client.send_message(message.channel, "Otherwise, here's a link to the annotated lyrics: \n{}".format(url))
      else:
        await client.send_message(message.channel, "I was unable to find the queried song. My apologies, I'm only a genius in name. " +
        "Check for typos and try again.")

  if message.content.upper().startswith('!SAVELYRICSFOR'):
    userID = message.author.id
    if message.content.find("-") == -1:
      await client.send_message(message.channel, "Sorry <@%s>, the song search must follow the [artist] - [song] structure. Type *!help* for more details. " % (userID))
    else:
      args = message.content.lower().replace("!savelyricsfor", "").split("-")
      a = args[0]
      s = args[1]
      await client.send_message(message.channel, "Searching for the lyrics to  *{}*  by  *{}* ...".format(s, a))
      song_to_save = api.search_song(s, a)
      if song_to_save:
        await client.send_message(message.channel, "Downloading the lyrics for  *{}*  by  *{}*  to the bot's host computer...".format(s, a))
        song_to_save.save_lyrics(format_='txt')

        await client.send_message(message.channel, "Here is a snippet of the lyrics you've requested: ")
        song_to_save_list = api.search_song(s, a).lyrics.split("\n")
        snippet = song_to_save_list[1:8]

        for line in snippet:
          if line == '':
            snippet.remove(line)
          else:
            await client.send_message(message.channel, "*{}*".format(line))
      else:
        await client.send_message(message.channel, "I was unable to find the queried song. My apologies, I'm only a genius in name. " +
        "Check for typos and try again.")

  if message.content.upper().startswith('!ALBUMFOR'):
    userID = message.author.id
    if message.content.find("-") == -1:
      await client.send_message(message.channel, "Sorry <@%s>, the song search must follow the [artist] - [song] structure. Type *!help* for more details. " % (userID))
    else: 
      args = message.content.lower().replace('!albumfor', "").split('-')
      a = args[0]
      s = args[1]
      await client.send_message(message.channel, "Finding the album for  *{}*  by  *{}* ...".format(s, a))
      song = api.search_song(s, a)
      if song:
        if song.album:
          album = song.album
          album_url = song.album_url
          await client.send_message(message.channel, "*{}*  is featured on the album  *{}*  by  *{}*".format(s, album, a))
          await client.send_message(message.channel, "Here's a link to the album on Genius: \n{}".format(album_url))
        else: 
          await client.send_message(message.channel, "I found the song... but I can't seem to find an associated album. Maybe it's a single?")
      else:
        await client.send_message(message.channel, "I was unable to find the queried song. My apologies, I'm only a genius in name. " +
        "Check for typos and try again.")

  if message.content.upper().startswith('!RELEASEDATEFOR'):
    userID = message.author.id
    if message.content.find("-") == -1:
      await client.send_message(message.channel, "Sorry <@%s>, the song search must follow the [artist] - [song] structure. Type *!help* for more details. " % (userID))
    else: 
      args = message.content.lower().replace('!releasedatefor', "").split('-')
      a = args[0]
      s = args[1]
      await client.send_message(message.channel, "Finding the release date for the track  *{}*  by  *{}* ...".format(s, a))
      song = api.search_song(s, a)
      if song:
        if song.year:
          release_date = song.year
          await client.send_message(message.channel, "Release date for  *{}*  by  *{}* :  *{}*".format(s, a, release_date))
        else:
          await client.send_message(message.channel, "I found the song... but I can't seem to determine the release date. I'm sorry, blame Genius xD")
      else:
        await client.send_message(message.channel, "I was unable to find the queried song. My apologies, I'm only a genius in name. " +
        "Check for typos and try again.")
client.run(TOKEN)