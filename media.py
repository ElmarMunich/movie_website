import webbrowser
class Movie():
# defines class Movie
    def __init__ (self, movie_title, poster_image, trailer_youtube, movie_director):
    # initializes the details for each movie with titel, artwork, trailer and director
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director = movie_director
