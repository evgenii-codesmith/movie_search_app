import requests
import collections

search = input('Enter movie to search:')
url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search)
resp = requests.get(url)
resp.raise_for_status()

movie_list = resp.json().get('hits')


MovieResult = collections.namedtuple(
    'MovieResult', "imdb_code, title, duration, director, year, rating, imdb_score, keywords, genres")

movies = [
    MovieResult(**movie)
    for movie in movie_list]

print('Found {} movies for search {}'.format(len(movies), search))
for m in movies:
    print('{} -- {}'.format(m.year, m.title))
