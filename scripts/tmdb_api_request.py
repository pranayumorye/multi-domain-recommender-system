import requests

api_key = "9f11bec2b71c7c8ce0ce44e3e1f1691d"


def make_popular_movies_request(page):
    base_url = "https://api.themoviedb.org/3/movie/popular"
    params = {"api_key": api_key,
              "page": page}

    res = requests.get(base_url, params=params)
    id_list = [result["id"] for result in res.json()["results"]]
    return id_list


def make_movie_details_request(movie_id):
    base_url = "https://api.themoviedb.org/3/movie/%d" % (movie_id)
    params = {"api_key": api_key}

    res = requests.get(base_url, params=params)
    return res.text


def main():
    with open("./out.json", "a") as f:
        for page in range(1, 100):
            print("Starting with page %d now" % (page))
            for movie_id in make_popular_movies_request(page):
                print("Movie no. %d" % (movie_id))
                f.write(make_movie_details_request(movie_id))
                f.write("\n")


main()
