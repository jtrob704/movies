import webbrowser


class Movie():
        """ This class creates an object called movies that accepts 4 parameters.
        movie title, movie storyline, URL for the poster image & a link to the
        YouTube trailer.
        """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


    def show_trailer(self):
        """This function call will open a web browser window and direct the user
        to the YouTube trailer.
        """
        webbrowser.open(self.trailer_youtube_url)
