import webbrowser

# Class for Movie object. This stores movie title, box art URL and a 
# YouTube link to the movie trailer
class Movie():
	# Initialize the class Movie with title, storyline, poster image, youtube URL
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		# Play trailer in a browser
		webbrowser.open(self.trailer_youtube_url)