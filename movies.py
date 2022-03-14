# import os
# import json
# import logging

# CUR_DIR = os.path.dirname(__file__)
# DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")

# def get_movies():
#     movies = []
#     with open(DATA_FILE, "r") as f:
#         movies_title = json.load(f)

#         movies = [Movie(movie_title) for movie_title in movies_title]
#         return movies



# class Movie:
#     def __init__(self, title):
#         self.title = title.title()

#     def __str__(self):
#         return self.title

#     def _get_movies(self):
#         with open(DATA_FILE, "r") as f:
#             return json.load(f)

#     def _write_movies(self, movies):
#         with open(DATA_FILE, "w") as f:
#             return json.dump(movies, f, indent=4)

#     # Recupérer la liste des films et ajouter des films.
#     def add_to_movies(self):
#         movies = self._get_movies()

#         if self.title not in movies:
#             movies.append(self.title)
#             self._write_movies(movies)
#             return True
#         else:
#             logging.warning(f"le film {self.title} est deja enregistté.")
#             return False

#     # Recupérer la liste des films et supprimer des films.
#     def remove_from_movies(self):
#         movies = self._get_movies()

#         if self.title in movies:
#           movies.remove(self.title)
#           self._write_movies(movies)



# if __name__ == "__main__":
#     movies = get_movies()
#     print(movies)


import json
import os

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")

def get_movies():
    movies_instances = []
    with open(DATA_FILE, "r") as f:
        movies = json.load(f)
        for movie_title in movies:
            movies_instances.append(Movie(movie_title))

        return movies_instances

class Movie:
    def __init__(self, title):
        self.title = title.title()

    def __str__(self):
        return self.title

    def _get_movies(self):
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    def _write_movies(self, movies):
        with open(DATA_FILE, "w") as f:
            json.dump(movies, f, indent=4)

    def add_to_movies(self):
        movies = self._get_movies()

        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            print(f"Le film {self.title} est déjà enregistré.")
            return False

    def remove_from_movies(self):
        movies = self._get_movies()

        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)

if __name__ == "__main__":
    m = Movie("harry potter")
    m.remove_from_movies()