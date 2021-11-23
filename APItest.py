import requests
import json


# To Get Top 20 Movies

"""url = "https://imdb8.p.rapidapi.com/title/get-popular-movies-by-genre"

querystring = {"genre": "/chart/popular/genre/adventure"}

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "8cc0defa2bmshe13b2dfa99419b6p11dfafjsnbab425a5ae48"
}

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
top_20_movies = response.text.split(',')[0:20]
top_20_movies_filtered = []
for i in top_20_movies:
    reversed = i[::-1]
    movie_title = reversed[10:1:-1]
    top_20_movies_filtered.append(movie_title)
print(top_20_movies_filtered)"""

# Response:

top_20_movies_filtered = ['tt10872600', 'tt9376612', 'tt9032400', 'tt1160419', 'tt2382320', 'tt4513678', 'tt0870154', 'tt3420504', 'tt7097896',
                          'tt6264654', 'tt2397461', 'tt0087182', 'tt5108870', 'tt3480822', 'tt6334354', 'tt0241527', 'tt2379713', 'tt2953050', 'tt0145487', 'tt4154796']

# To get Details of Top 20 movies

"""url = "https://imdb8.p.rapidapi.com/title/get-details"


top_20_movies_details = []
for i in top_20_movies_filtered:
    print(i)
    movie_details = {}
    url = "https://imdb8.p.rapidapi.com/title/get-details"

    querystring = {"tconst": i}

    headers = {
        'x-rapidapi-host': "imdb8.p.rapidapi.com",
        'x-rapidapi-key': "8cc0defa2bmshe13b2dfa99419b6p11dfafjsnbab425a5ae48"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    res = json.loads(response.text)
    movie_details["imageURL"] = res["image"]["url"]
    movie_details["type"] = res["titleType"]
    movie_details["title"] = res["title"]
    try:
        movie_details["startYear"] = res["seriesStartYear"]
        movie_details["endYear"] = res["seriesEndYear"]
    except KeyError:
        movie_details["year"] = res["year"]

    top_20_movies_details.append(movie_details)
print(top_20_movies_details)"""
# Response:
top_20_movies_details = [{'imageURL': 'https://m.media-amazon.com/images/M/MV5BMDUzNWJhZWQtYzU3Zi00M2NjLThjZjEtMTRmMjRmNzBmMWI2XkEyXkFqcGdeQXVyODIyOTEyMzY@._V1_.jpg', 'type': 'movie', 'title': 'Spider-Man: No Way Home', 'year': 2021}, {'imageURL': 'https://m.media-amazon.com/images/M/MV5BNTliYjlkNDQtMjFlNS00NjgzLWFmMWEtYmM2Mzc2Zjg3ZjEyXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_.jpg', 'type': 'movie', 'title': 'Shang-Chi and the Legend of the Ten Rings', 'year': 2021}, {'imageURL': 'https://m.media-amazon.com/images/M/MV5BMTExZmVjY2ItYTAzYi00MDdlLWFlOWItNTJhMDRjMzQ5ZGY0XkEyXkFqcGdeQXVyODIyOTEyMzY@._V1_.jpg', 'type': 'movie', 'title': 'Eternals', 'year': 2021}, {'imageURL': 'https://m.media-amazon.com/images/M/MV5BN2FjNmEyNWMtYzM0ZS00NjIyLTg5YzYtYThlMGVjNzE1OGViXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_.jpg', 'type': 'movie', 'title': 'Dune', 'year': 2021}, {'imageURL': 'https://m.media-amazon.com/images/M/MV5BYWQ2NzQ1NjktMzNkNS00MGY1LTgwMmMtYTllYTI5YzNmMmE0XkEyXkFqcGdeQXVyMjM4NTM5NDY@._V1_.jpg', 'type': 'movie', 'title': 'No Time to Die', 'year': 2021}, {'imageURL': 'https://m.media-amazon.com/images/M/MV5BMmZiMjdlN2UtYzdiZS00YjgxLTgyZGMtYzE4ZGU5NTlkNjhhXkEyXkFqcGdeQXVyMTEyMjM2NDc2._V1_.jpg', 'type': 'movie', 'title': 'Ghostbusters: Afterlife', 'year': 2021}, {'imageURL': 'https://m.media-amazon.com/images/M/MV5BNDE1MGRlNTQtZjc4ZC00MTI0LWEwY2MtODk1YTM2NmFmYTNmXkEyXkFqcGdeQXVyODk4OTc3MTY@._V1_.jpg', 'type': 'movie', 'title': 'Jungle Cruise', 'year': 2021}, {'imageURL': 'https://m.media-amazon.com/images/M/MV5BZTMxYjk3MmItMzk1OC00NmRhLThlMjYtNmQyNzA0MzgxMWI2XkEyXkFqcGdeQXVyMDM2NDM2MQ@@._V1_.jpg', 'type': 'movie', 'title': 'Finch', 'year': 2021}, {'imageURL': 'https://m.media-amazon.com/images/M/MV5BYTc3ZTAwYTgtMmM4ZS00MDRiLWI2Y2EtYmRiZmE0YjkzMGY1XkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_.jpg', 'type': 'movie', 'title': 'Venom: Let There Be Carnage', 'year': 2021}, {'imageURL': 'https://m.media-amazon.com/images/M/MV5BOTY2NzFjODctOWUzMC00MGZhLTlhNjMtM2Y2ODBiNGY1ZWRiXkEyXkFqcGdeQXVyMDM2NDM2MQ@@._V1_.jpg', 'type': 'movie',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           'title': 'Free Guy', 'year': 2021}, {'imageURL': 'https://m.media-amazon.com/images/M/MV5BZGIxYTU5MzctY2MzNS00MTRhLWEwM2UtY2Q5Mzk3OTAzMzcwXkEyXkFqcGdeQXVyMTEyMjM2NDc2._V1_.jpg', 'type': 'movie', 'title': 'Clifford the Big Red Dog', 'year': 2021}, {'imageURL': 'https://m.media-amazon.com/images/M/MV5BYTAzYzNlMDMtMGRjYS00M2UxLTk0MmEtYmE4YWZiYmEwOTIwL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNzc5MjA3OA@@._V1_.jpg', 'type': 'movie', 'title': 'Dune', 'year': 1984}, {'imageURL': 'https://m.media-amazon.com/images/M/MV5BNjIxMDcxMGQtNTViOC00MWM0LWFjYjItNDNmNzRkZThlMmZjXkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_.jpg', 'type': 'movie', 'title': 'Morbius', 'year': 2022}, {'imageURL': 'https://m.media-amazon.com/images/M/MV5BNjRmNDI5MjMtMmFhZi00YzcwLWI4ZGItMGI2MjI0N2Q3YmIwXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_.jpg', 'type': 'movie', 'title': 'Black Widow', 'year': 2021}, {'imageURL': 'https://m.media-amazon.com/images/M/MV5BNGM3YzdlOWYtNjViZS00MTE2LWE1MWUtZmE2ZTcxZjcyMmU3XkEyXkFqcGdeQXVyODEyMTI1MjA@._V1_.jpg', 'type': 'movie', 'title': 'The Suicide Squad', 'year': 2021}, {'imageURL': 'https://m.media-amazon.com/images/M/MV5BNjQ3NWNlNmQtMTE5ZS00MDdmLTlkZjUtZTBlM2UxMGFiMTU3XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_.jpg', 'type': 'movie', 'title': "Harry Potter and the Sorcerer's Stone", 'year': 2001}, {'imageURL': 'https://m.media-amazon.com/images/M/MV5BOWQ1MDE1NzgtNTQ4OC00ZjliLTllZDAtN2IyOTVmMTc5YjUxXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg', 'type': 'movie', 'title': 'Spectre', 'year': 2015}, {'imageURL': 'https://m.media-amazon.com/images/M/MV5BNjE5NzA4ZDctOTJkZi00NzM0LTkwOTYtMDI4MmNkMzIxODhkXkEyXkFqcGdeQXVyNjY1MTg4Mzc@._V1_.jpg', 'type': 'movie', 'title': 'Encanto', 'year': 2021}, {'imageURL': 'https://m.media-amazon.com/images/M/MV5BZDEyN2NhMjgtMjdhNi00MmNlLWE5YTgtZGE4MzNjMTRlMGEwXkEyXkFqcGdeQXVyNDUyOTg3Njg@._V1_.jpg', 'type': 'movie', 'title': 'Spider-Man', 'year': 2002}, {'imageURL': 'https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_.jpg', 'type': 'movie', 'title': 'Avengers: Endgame', 'year': 2019}]
