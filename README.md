# Genius-Bot

Genius Bot is an autonomous discord bot that uses the LyricsGenius framework to scrape song data and other artist metadata from the Genius
website via the Genius web API. At it's most basic level, the Bot can recite the lyrics for your favorite songs. With more nuanced queries,
the bot can provide various statistics about an artist's catalog of music.

# How It Works

Keywords:

!lyricsfor [artist] - [song]:
  *The bot will retrieve and recite the lyrics for the queried song*
  


# Tech Stack Details

LyricsGenius

  Backend python framework that uses the Genius Web API to retrieve music data.
  The LyricsGenius uses the following frameworks/libraries:
  
  
    BeautifulSoup
    requests (HTTP requests)
    urllib2 (format search requests)
    
discord.py

  Api wrapper for discord written in python. Allows you to program discord bot/chat logs with python.
 
