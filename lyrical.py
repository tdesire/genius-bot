import lyricsgenius as genius
api = genius.Genius('I77pPvz_lAoG8k_9DJAol0bUOWQn0Xtngc1n2ytRE-J1oTeHKJfnIlPa3pZ3vTfp')

def get_lyrics():
  """This function allows the user to search for specific song lyrics by inputing the artist and song name"""
  a = input('Enter an artist`s name: (ex: Radiohead)')
  a
  s = input('Enter a song by this artist: (Weird Fishes/Arpeggi)')
  s

  song = str(api.search_song(s, a))
  print(song)

def get_artist_data():
  """This function allows the user to get data for their favorite artist's top tracks"""
  print('How well do you know your favorite artist`s music??! Let`s see if you can identify some of their best tracks!')
  a = input('Enter an artist`s name: (ex: Kendrick Lamar) ')
  artist = api.search_artist(a, max_songs=3)
  print(artist.songs[0])
  song = str(artist.songs.pop())
  print('Here comes the lyrics...')
  print(song[50:])
  answer = input('Name this song: ')
  if song.upper().index(answer.upper()) == 0:
    print('COrr!')
  else:
    print('Correct!')

if __name__ == '__main__':
  # get_lyrics()
  get_artist_data()
