# cd /users/elmar/desktop/NDBeginner/Python
import fresh_tomatoes
import media

alexis_sorbas = media.Movie("Alexis Sorbas",
                             "A story about an Basil an English-Greek writer and Zorba a Greek-Macedonian peasant",
                             "https://upload.wikimedia.org/wikipedia/en/b/b4/Zorba_book.jpg",
                             "https://www.youtube.com/watch?v=1cJfIbMbw_4")

sleepnees_in_seattle = media.Movie("Sleepness in Seattle",
                                     "Sam who has lost his wife Maggie to cancer is persuaded by his son Jonah to speak in a radio show.",
                                     "https://upload.wikimedia.org/wikipedia/en/e/e1/Sleepless_in_seattle.jpg",
                                     "https://www.youtube.com/watch?v=-Lj2U-cmyek")


pulp_fiction = media.Movie("Pulp Fiction",
                            "An interwoven story about Vincent Vega and Jules Winnfield, two hitman who work for Marcellus Wallace",
                            "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
                            "https://www.youtube.com/watch?v=WSLMN6g_Od4")

darjeeling_limited = media.Movie("The Darjeeling Limited",
                                  "Three very different brothers try to find together in a journey through India",
                                  "https://upload.wikimedia.org/wikipedia/en/1/1e/Darjeeling_Limited_Poster.jpg",
                                  "https://www.youtube.com/watch?v=aO1bYukdvLI")

what_the_health = media.Movie("What the Health",
                               "A documentary about health and eating habits, industry and goverment.",
                               "https://upload.wikimedia.org/wikipedia/en/8/8a/What_the_Health_cover_art.jpg",
                               "https://www.youtube.com/watch?v=Jf44vLndiRM")

lost_in_translation = media.Movie("Lost in Translation",
                                   "A story about Bob and Charlotte, who are on a trip to Tokyo and are in a disillusioned relationsships",
                                   "https://upload.wikimedia.org/wikipedia/en/4/4c/Lost_in_Translation_poster.jpg",
                                   "https://www.youtube.com/watch?v=sU0oZsqeG_s")


#print (alexis_sorbas.title)
#print (alexis_sorbas.storyline)
#print (alexis_sorbas.poster_image_url)
#print (alexis_sorbas.trailer_youtube_url)

#print (pulp_fiction.title)
#print (pulp_fiction.storyline)
#pulp_fiction.show_trailer()

movies = [alexis_sorbas, sleepnees_in_seattle, pulp_fiction, darjeeling_limited, what_the_health, lost_in_translation]
#fresh_tomatoes.open_movies_page(movies)

print (media.Movie.VALID_RATINGS)
print (media.Movie.__doc__)
