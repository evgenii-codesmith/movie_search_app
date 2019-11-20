from movie_svc import get_movies
import requests.exceptions


def main():
    print_header()
    search_event_loop()


def print_header():
    print('--------------------------')
    print('       Movie search app   ')
    print('--------------------------')
    print()


def search_event_loop():
    search = ''

    while search != 'x':
        try:
            search = input('Enter movie name to search or \'x\' to exit: ')
            if search == 'x':
                print('Exiting...')
                break
            elif not search or not search.strip():
                raise ValueError()
            movies = get_movies(search)
            print('Found {} movies for search {}'.format(len(movies), search))
            for m in movies:
                print('{} -- {}'.format(m.year, m.title))
            print()
        except ValueError:
            print('Search value required')
        except requests.exceptions.ConnectionError as ce:
            print('Network error: {}'.format(ce))
        except Exception as e:
            print('General error: {}'.format(e))


if __name__ == '__main__':
    main()
