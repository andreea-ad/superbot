from firebase import firebase
import imdb
import random

class MoviePicker:

  def __init__(self):
    self.firebase_client = firebase.FirebaseApplication("https://superbot-1518d-default-rtdb.firebaseio.com/", None)
    self.towatch_dictionary = self.firebase_client.get('/towatch', None)
    self.towatch_dictionary.pop(0)
    print(self.towatch_dictionary)

  def pick_movie(self):
    current_movie_index = random.randint(0, len(self.towatch_dictionary)-1)
    print(current_movie_index)
    current_movie_title = self.towatch_dictionary[current_movie_index]

    imdb_retriever = ImdbInfoRetriever(current_movie_title)
    return imdb_retriever.get_movie_data()

class ImdbInfoRetriever:
  def __init__(self, movie_title):
    self.imdb_client = imdb.IMDb()
    self.movie_title = movie_title

  def get_movie_data(self):
    movie = self.get_movie()
    return movie.summary()

  def get_movie(self):
    movies = self.imdb_client.search_movie(self.movie_title)
    movie_id = movies[0].getID()
    movie = self.imdb_client.get_movie(movie_id)
    return movie
