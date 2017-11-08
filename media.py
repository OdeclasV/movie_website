import webbrowser

class Movie():
	''' This class provides a way to store movie related information '''

	'''This is a constant variable (class variable), and Google StyleGuide says that these type of variables should be spelled out in all caps'''
	VALID_RATINGS = ["G", "PG", "PG-13", "R"] 


	def __init__(self, movie_title,movie_storyline, poster_image, trailer_youtube, date, numb_of_times_watched): 	
		# NOTE:__ underscores tell that this is a reserved word in python
	
		'''Function that constructs instances of Movie class for each movie in the website. Arguments are assigned to corresponding instance variables below. 
		Arguments:
			movie_title(str): Name of the movie
			movie_storyline(str): Brief description of the movie and its plot
			poster_image(str): ULR of movie posting from Wikipedia (if available)
			trailer_youtube(str): URL of movie trailer from YouTube (if available)
			date(number): Year in which the movie was relased
			numb_of_times_watched (number): Total number of times I've seen that movie'''

		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.launch_date = date
		self.times_watched = numb_of_times_watched

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url) # opens browser to show movie trailer





	