import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story","A story of a boy and his toys that come to life",
	                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", " A marine on an allien planet",
	                    "https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
	                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

avenger = media.Movie("Avengers", "Age of Ultron",
	                    	"http://www.showbiz411.com/wp-content/uploads/2015/04/avengers.jpg",
	                    	"https://www.youtube.com/watch?v=bMP-FLmiIM0")
mad_max = media.Movie("Mad Max", "Fury Road",
	                    "http://ia.media-imdb.com/images/M/MV5BMTUyMTE0ODcxNF5BMl5BanBnXkFtZTgwODE4NDQzNTE@._V1_SX640_SY720_.jpg",
	                    "https://www.youtube.com/watch?v=woHTUsl66BY")
imitation = media.Movie("The Imitation Game","Real life story of legendary cryptanalyst Alan Turing",
							"http://ia.media-imdb.com/images/M/MV5BNDkwNTEyMzkzNl5BMl5BanBnXkFtZTgwNTAwNzk3MjE@._V1_SX640_SY720_.jpg",
							"https://www.youtube.com/watch?v=Sn-7SNrQWMo") 

gone_girl = media.Movie("Gone Girl","Did Nick Dunne kill his wife? ",
							"http://ia.media-imdb.com/images/M/MV5BMTk0MDQ3MzAzOV5BMl5BanBnXkFtZTgwNzU1NzE3MjE@._V1_SX640_SY720_.jpg",
							"https://www.youtube.com/watch?v=Ym3LB0lOJ0o")
movies = ["toy_story","avatar","avenger","mad_max","imitation","gone_girl"]
fresh_tomatoes.open_movies_page(movies)


