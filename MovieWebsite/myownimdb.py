import media

toystory = media.Movie("Toy Story",
                 "Boy and his toys",
                 "https://goo.gl/images/xqbCiB",
                 "https://www.youtube.com/watch?v=KYz2wyBy3kc")
##print(toystory.poster_image_url)
##webbrowser.open(toystory.trailer_youtube_url)
avatar = media.Movie("Avatar",
               "A marine in an alien planet",
               "https://commons.wikimedia.org/wiki/File:Avatars.jpg",
               "https://www.youtube.com/watch?v=5PSNL1qE6VY")


##print (avatar.storyline)
##avatar.show_trailer()

starwars = media.Movie("Star Wars - The Force Awakens",
                       "It is freaking Star Wars !!!",
                       "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
                       "https://www.youtube.com/watch?v=sGbxmsDFVnE")

starwars.show_trailer()
