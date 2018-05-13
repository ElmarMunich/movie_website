# cd /users/elmar/desktop/movie_website
import fresh_tomatoes
# imports python file for creating the html page for the movie trailers
import media
# imports class Movie from file media.py

manhattan = media.Movie("Manhattan",
                             "https://upload.wikimedia.org/wikipedia/en/f/f3/Manhattan-poster01.jpg",
                             "https://www.youtube.com/watch?v=JEoEGW4Hb9w",
                             "Woody Allan")
# creates a single instance of the class movie

sleepnees_in_seattle = media.Movie("Sleepness in Seattle",
                                     "https://upload.wikimedia.org/wikipedia/en/e/e1/Sleepless_in_seattle.jpg",
                                     "https://www.youtube.com/watch?v=-Lj2U-cmyek",
                                     "Nora Ephron")


pulp_fiction = media.Movie("Pulp Fiction",
                            "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
                            "https://www.youtube.com/watch?v=WSLMN6g_Od4",
                            "Quentin Tarantino")

darjeeling_limited = media.Movie("The Darjeeling Limited",
                                  "https://upload.wikimedia.org/wikipedia/en/1/1e/Darjeeling_Limited_Poster.jpg",
                                  "https://www.youtube.com/watch?v=aO1bYukdvLI",
                                  "Wes Anderson")

what_the_health = media.Movie("What the Health",
                               "https://upload.wikimedia.org/wikipedia/en/8/8a/What_the_Health_cover_art.jpg",
                               "https://www.youtube.com/watch?v=Jf44vLndiRM",
                               "Kip Andersen, Keegan Kuhn")

groundhog_day = media.Movie("Groundhog Day",
                                   "https://upload.wikimedia.org/wikipedia/en/b/b1/Groundhog_Day_%28movie_poster%29.jpg",
                                   "https://www.youtube.com/watch?v=GncQtURdcE4",
                                   "Harold Ramis")



movies = [manhattan, sleepnees_in_seattle, pulp_fiction, darjeeling_limited, what_the_health, groundhog_day]
fresh_tomatoes.open_movies_page(movies)
# a list of all movies for which trailers will be created
