import fresh_tomatoes
import media

# Create an instance for each movie to be displayed and store the information in a list
toy_story = media.Movie("Toy Story","A story of a boy and his toys that come to life","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar","A marine on an alien planet","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=1EnL7vUmvQ4")

independence_day = media.Movie("Independence Day", "Aliens invade earth", "https://upload.wikimedia.org/wikipedia/en/b/bb/Independence_day_movieposter.jpg", "https://www.youtube.com/watch?v=NZZvtQtdbzM")

movies = [toy_story, avatar, independence_day]

# Pass movies variable into open_movie_page method in fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)