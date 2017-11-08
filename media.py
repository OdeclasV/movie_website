import webbrowser

class Movie():
	"""This class provides a way to store movie related information"""

	VALID_RATINGS = ["G", "PG", "PG-13", "R"] # this is a constant variable (class variable), and Google StyleGuide says that these type of variables should be spelled out in all caps

	def __init__(self, movie_title,movie_storyline, poster_image, trailer_youtube, date, numb_of_times_watched): # __ underscores tell that this is a reserved word in python
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.launch_date = date
		self.times_watched = numb_of_times_watched

	def show_trailer(self):
		'''opens browser to show movie trailer '''
		webbrowser.open(self.trailer_youtube_url)





	