import media
import fresh_tomatoes

"""Define Movie classes"""
mast_comm = media.Movie("Master and Commander",
                        "An English captain is hunted by a French Privateer",
                        "http://upload.wikimedia.org/wikipedia/en/thumb/b/bf/Master_and_Commander-The_Far_Side_of_the_World_poster.png/220px-Master_and_Commander-The_Far_Side_of_the_World_poster.png",
                        "https://www.youtube.com/watch?v=pFeCVCKYo4Y",
                        "http://en.wikipedia.org/wiki/Master_and_Commander:_The_Far_Side_of_the_World" )
s_wars = media.Movie("Star Wars:A New Hope",
                        "A boy and his laser sword",
                        "http://upload.wikimedia.org/wikipedia/en/thumb/8/87/StarWarsMoviePoster1977.jpg/220px-StarWarsMoviePoster1977.jpg",
                        "https://www.youtube.com/watch?v=1g3_CFmnU7k",
                        "http://en.wikipedia.org/wiki/Star_Wars_(film)" )
fut_folk = media.Movie("History of Future Folk",
                        "Aliens that like Folk Music",
                        "http://ia.media-imdb.com/images/M/MV5BNzA3MDI3MzAxMl5BMl5BanBnXkFtZTcwNDY2Mjc0OQ@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                        "https://www.youtube.com/watch?v=fZrDALCsKwI",
                        "http://en.wikipedia.org/wiki/Future_Folk" )
istellar = media.Movie("Insterstellar",
                        "Time Travel, Space and lots of Dust",
                        "http://upload.wikimedia.org/wikipedia/en/thumb/b/bc/Interstellar_film_poster.jpg/220px-Interstellar_film_poster.jpg",
                        "https://www.youtube.com/watch?v=0vxOhd4qlnA",
                        "http://en.wikipedia.org/wiki/Interstellar_%28film%29" )

"""Put movie classes into list for web site"""
movies = [mast_comm,s_wars,fut_folk,istellar]

"""Open webpage with movie list"""
fresh_tomatoes.open_movies_page(movies)

