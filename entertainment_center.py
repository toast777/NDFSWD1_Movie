import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio","http://en.wikipedia.org/wiki/Toy_Story" )
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                        "A marine on a alien planet",
                        "http://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=cRdxXPV9GNQ","http://en.wikipedia.org/wiki/Avatar_(2009_film)" )
movies = [toy_story,avatar]
fresh_tomatoes.open_movies_page(movies)

