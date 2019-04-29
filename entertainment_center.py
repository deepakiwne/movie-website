import fresh_tomatoes
import media

# Add favourite movie details
toy_story = media.Movie("Toy Story",
    "A story of a boy and his toys that come to life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
    "A marine on an alien planet",
    "https://i.pinimg.com/originals/c3/2e/40/c32e40b633ff92a2d3048f5ce8570c90.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

finding_nemo = media.Movie("Finding Nemo",
    "The overprotective ocellaris clownfish named Marlin who, along with a regal blue tang named Dory, searches for his abducted son Nemo all the way to Sydney Harbour",
    "https://i.pinimg.com/originals/0e/90/87/0e90874cf75ddb0b85205934fade8d10.jpg",
    "https://www.youtube.com/watch?v=3JnKU9Stmyw")

notebook = media.Movie("Notebook",
    "A young couple who fall in love in the 1940s",
    "https://c8.alamy.com/comp/B7W5NB/the-notebook-year-2004-usa-director-nick-cassavetes-movie-poster-fr-B7W5NB.jpg",
    "https://www.youtube.com/watch?v=FC6biTjEyZw")

frozen = media.Movie("Frozen",
    "A fearless princess who sets off on a journey to find her estranged sister, whose icy powers have inadvertently trapped their kingdom in eternal winter",
    "https://m.media-amazon.com/images/M/MV5BMTQ1MjQwMTE5OF5BMl5BanBnXkFtZTgwNjk3MTcyMDE@._V1_.jpg",
    "https://www.youtube.com/watch?v=TbQm5doF_Uc")

boss_baby = media.Movie("Boss Baby",
    "A baby who is a secret agent in the war for adults' love between babies and puppies",
    "https://images-na.ssl-images-amazon.com/images/I/61aby5yjHDL._SY606_.jpg",
    "https://www.youtube.com/watch?v=tquIfapGVqs")

# Add movies in a list
movies = [toy_story, avatar, finding_nemo, notebook, frozen, boss_baby]
fresh_tomatoes.open_movies_page(movies)