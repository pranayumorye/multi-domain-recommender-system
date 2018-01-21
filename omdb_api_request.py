import requests
import json

def obtain_movie_info(movie_name):
    url = "http://www.omdbapi.com"
    api_key = "8a041c47"
    params_dict = {"apikey": api_key, "t": movie_name}

    response = requests.get(url, params = params_dict)
    decoder = json.JSONDecoder()
    return decoder.decode(response.text)

def main():
    movies = ["inception", "the dark knight", "the prestige", "harry potter and the prisoner of azkaban"]
    for movie in movies:
        movie_info_dict = obtain_movie_info(movie)
        keys = ["Title", "Genre", "Actors"]
        print([movie_info_dict[key] for key in keys])

main()
