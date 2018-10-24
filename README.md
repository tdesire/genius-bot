# Genius-Bot

Genius Bot is a responsive discord bot that uses the LyricsGenius framework to scrape song data and other artist metadata from the Genius website via the Genius web API. At it's most basic level, the Bot can recite the lyrics for your favorite songs. With more nuanced queries, the bot can provide various statistics about an artist's catalog of music.

# How It Works

Keywords:

!lyricsfor [artist] - [song]:
  *The bot will retrieve and recite the lyrics for the queried song*


!savelyricsfor [artist] - [song]:
  *The bot will retrieve and download the lyrics of the queried song as a txt file to the local computer hosting the bot*


!albumfor [artist] - [song]:
 *The bot will respond with the album that features the queried song*


!releasedatefor [artist] - [song]:
 *The bot will respond with the release date of the queried song*


# Tech Stack Details

LyricsGenius

  Backend python API wrapper that uses the Genius Web API to scrap music data from the Genius.com website.
  
  LyricsGenius uses the following frameworks/libraries:
  
  
    BeautifulSoup
    requests (HTTP requests)
    urllib2 (format search requests)
    
  Link to LyricsGenius GitHub Repo:
  
  https://github.com/johnwmillr/LyricsGenius
    
discord.py

  Api wrapper for discord written in python. Allows the user to program discord bot/chat logs with python.
  
  Link to discord.py GitHub repo:
  
  https://github.com/Rapptz/discord.py
 
