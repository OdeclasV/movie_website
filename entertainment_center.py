import fresh_tomatoes
import media

'''NOTE: limit line lenght to less than 72 characters. Notice how within different instances of movie, I break up long line of codes apart, specially url links to poster images. '''
toy_story = media.Movie("Toy Story",
						"A story of a boy a his toys that come to life",
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc",
						1995,
						5)

avatar = media.Movie("Avatar",
					"A marine on an alien planet",
					"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					"https://www.youtube.com/watch?v=5PSNL1qE6VY",
					2009,
					2)

james_bond = media.Movie("Casino Royale",
						"Casino Royale takes place at the beginning of Bond's career as Agent 007"
						"just as he is earning his licence to kill",
						"https://upload.wikimedia.org/wikipedia/en/1/15/"
						"Casino_Royale_2_-_UK_cinema_poster.jpg",
						"https://www.youtube.com/watch?v=fl5WHj0bZ2Q",
						2006,
						7)

moana = media.Movie("Moana",
					"Little girl goes on a adventure at sea",
					"https://upload.wikimedia.org/wikipedia/en/2/26/"
					"Moana_Teaser_Poster.jpg",
					"https://www.youtube.com/watch?v=LKFuXETZUsI",
					2016,
					6)

grand_budapest = media.Movie("The Grand Budapest Hotel",
							"The fantastical history of the Grand Budapest Hotel",
							"https://upload.wikimedia.org/wikipedia/en/a/a6/"
							"The_Grand_Budapest_Hotel_Poster.jpg",
							"https://www.youtube.com/watch?v=1Fg5iWmQjwk",
							2013,
							5)
dope = media.Movie("Dope",
				   "Highschool students create a business",
				   "https://vignette.wikia.nocookie.net/to-hollywood-and-beyond/"
				   "images/6/63/Dope2015.jpg/"
				   "revision/latest/scale-to-width-down/250?cb=20151208012740",
				   "https://www.youtube.com/watch?v=L41xwM8tIRQ",
				   2015,
				   3)

movies = [toy_story,avatar,james_bond,moana,grand_budapest,dope]
fresh_tomatoes.open_movies_page(movies) # this calls function open_movies_page inside fresh_tomoatoes


