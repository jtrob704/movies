import fresh_tomatoes
import media

# These created objects will store each movie's title, description, album art
# and a link to its YouTube trailer.
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=1EnL7vUmvQ4")

independence_day = media.Movie("Independence Day",
                               "Aliens invade earth",
                               "https://upload.wikimedia.org/wikipedia/en/b/bb/Independence_day_movieposter.jpg",
                               "https://www.youtube.com/watch?v=NZZvtQtdbzM")

movies = [toy_story, avatar, independence_day]

# This function call opens a page of movies generated from the input, an
# array of movie instances.
fresh_tomatoes.open_movies_page(movies)
