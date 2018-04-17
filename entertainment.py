import fresh_tomatoes  # imported fresh tomato
import media  # imported media

# Creating movie tiles for webpage
ANNABELLE_CREATION = media.Movie(
                                 "Annabelle Creation",
                                 "12 years after the tragic \
                                 death of their little girl, \
                                 a dollmaker and his wife \
                                 welcome a nun and several girls \
                                 from a shuttered orphanage into their home, \
                                 where they soon become the target of the \
                                 dollmaker's possessed creation, \
                                 Annabelle",
                                 "https://goo.gl/LQhqs2",
                                 "https://www.youtube.com/watch?v=EjZkJa6Z-SY")
The_Conjuring = media.Movie(
                            "The Conjuring",
                            "Paranormal investigators Ed and \
                            Lorraine Warren work to help a family \
                            terrorized by a dark presence in their farmhouse.",
                            "https://goo.gl/Qhg5Wv",
                            "https://www.youtube.com/watch?v=k10ETZ41q5o")
the_school = media.Movie(
                         "The School",
                         "When a doctor looking for her missing child \
                         awakens to find herself in an abandoned school, \
                         she must survive the supernatural terror and face \
                         her own demons if she is to find the truth about \
                         where her son is.",
                         "https://goo.gl/6Hn5d4",
                         "https://www.youtube.com/watch?v=ADP2PxRq9M8")
movies = [ANNABELLE_CREATION, The_Conjuring, the_school]
fresh_tomatoes.open_movies_page(movies)
