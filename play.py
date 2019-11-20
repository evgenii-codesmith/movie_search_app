import requests
import collections

search = input('Enter movie to search:')
url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search)
resp = requests.get(url)

movie_data = resp.json()['hits']

MovieRSesult = collections.namedtuple(
    'MovieResult', "imdb_code, title, director, duration, genres, rating, year, imdb_score")

movies = []
for item in movie_data:
    m = MovieRSesult(
        imdb_code=item.get('imdb_code'),
        title=item.get('title'),
        director=item.get('director'),
        duration=item.get('duration'),
        genres=item.get('genres'),
        rating=item.get('rating', 0),
        year=item.get('year', 0),
        imdb_score=item.get('imdb_score', 0.0)

    )
    movies.append(m)

print('Found {} movies for search {}'.format(len(movies), search))
for m in movies:
    print('{} -- {}'.format(m.year, m.title))
