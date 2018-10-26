# Genius-Bot

Genius Bot is a responsive discord bot that uses the LyricsGenius framework to scrape song data and other artist metadata from the Genius website via the Genius web API. At it's most basic level, the Bot can recite the lyrics for your favorite songs. With more nuanced queries, the bot can provide various info about an artist's catalog of music.

## How It Works

Keywords:

!lyricsfor [artist] - [song]:
  *The bot will retrieve and recite the lyrics for the queried song, and provide a link to the annotated lyrics*


!savelyricsfor [artist] - [song]:
  *The bot will retrieve and download the lyrics for the queried song as a txt file to the local computer hosting the bot. 
  The file will be saved to the directory where the script file lives.*


!albumfor [artist] - [song]:
 *The bot will respond with the album that features the queried song, and provide a link to the Genius page for the specific album*


!releasedatefor [artist] - [song]:
 *The bot will respond with the release date of the queried song*

## Setup
*The following instructions are a brief guide for hosting your own Genius Bot*

1. Both LyricsGenius and Discord.py require Python3.
2. Clone this repo and use pip to install all relevant dependencies (ex: python -m pip install).
3. You will need to sign up for an account with Genius in order to authorize access to their web API. The provided authorization key will be used to authenticate all requests sent by the LyricsGenius API wrapper. Details can be found here:
    https://docs.genius.com/
 *Add the genius auth token to the config_sample.py file, and modify the genius-bot.py file accordingly (see lines 4, 6, and 7)*
4. Similarly, you will need an account with discord in order to create and instantiate a new bot application. During this process, you will define bot permissions, and generate an OAuth2 url that you will use to add your bot to a discord server.
5. During the discord bot setup process you will retrieve a token that you'll use to wire up the genius-bot script to your new bot. 
 *Add the bot key to the config_sample.py file. Similarly, modify the genius-bot.py file (see lines 13 and 14)*
6. Lastly, run the script file in terminal (ex: python genius-bot.py) to boot-up your bot, and join the specified server in discord. From there you can start interacting with your own personal Genius Bot!

## Tech Stack Details
LyricsGenius:

   Backend python API wrapper that uses the Genius Web API to scrape music data from the Genius.com website.
  
   LyricsGenius uses the following frameworks/libraries:
  
  
  
    BeautifulSoup (Parse http response data);
    requests (HTTP requests);
    urllib2 (format search requests)
    
   Link to LyricsGenius GitHub Repo:
  
     https://github.com/johnwmillr/LyricsGenius
    
discord.py:
* Api wrapper for discord written in python. Allows the user to program discord bot/chat logs with python.
* Link to discord.py GitHub repo:

   https://github.com/Rapptz/discord.py
 
