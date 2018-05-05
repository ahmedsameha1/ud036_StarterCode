import webbrowser


class Movie():
    # Define the constructor
    def __init__(self, movie_title, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # This method opens the web browser and displays the video
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
