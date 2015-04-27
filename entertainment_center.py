import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio" )
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                        "A marine on a alien planet",
                        "http://en.wikipedia.org/wiki/Avatar_%282009_film%29",
                        "https://www.youtube.com/watch?v=cRdxXPV9GNQ" )
movies = [toy_story,avatar]
fresh_tomatoes.open_movies_page(movies)

