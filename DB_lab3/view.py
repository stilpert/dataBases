class View(object):

    @staticmethod
    def display_studios(studios):
        print("==================================================================")
        for studio in studios:
            print("Id: {0}, name: {1}, country: {2}".format(studio.id, studio.name, studio.country))
        print("==================================================================")

    @staticmethod
    def display_studio(studio):
        print("==================================================================")
        print("Id: {0}, name: {1}, country: {2}".format(studio.id, studio.name, studio.country))
        print("==================================================================")

    @staticmethod
    def display_actors(actors):
        print("==================================================================")
        for actor in actors:
            print("Id: {0}, name: {1}, gender: {2}, age: {3}"
                  .format(actor.id, actor.full_name, actor.gender, actor.age))
        print("==================================================================")

    @staticmethod
    def display_actor(actor):
        print("==================================================================")
        print("Id: {0}, name: {1}, gender: {2}, age: {3}"
              .format(actor.id, actor.full_name, actor.gender, actor.age))

    @staticmethod
    def display_movies(movies):
        print("==================================================================")
        for movie in movies:
            print("Id: {0}, name: {1}, genre: {2}, budget: {3}".format(movie.id, movie.name, movie.genre, movie.budget))
            print("Description: {0}".format(movie.description))
        print("==================================================================")

    @staticmethod
    def display_movie(movie):
        print("==================================================================")
        print("Id: {0}, name: {1}, genre: {2}, budget: {3}".format(movie.id, movie.name, movie.genre, movie.budget))
        print("Description: {0}".format(movie.description))

    @staticmethod
    def display_success():
        print("==================================================================")
        print("Operation completed successfully")
        print("==================================================================")

    @staticmethod
    def display_error():
        print("==================================================================")
        print("Operation wasn't completed")
        print("==================================================================")

    @staticmethod
    def display_no_results():
        print("==================================================================")
        print("There is no results")
        print("==================================================================")
