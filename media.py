import webbrowser
class Movie():
# defines class Movie         
    def __init__ (self, movie_title, poster_image, trailer_youtube, movie_director):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director = movie_director
