

class View(object):

    @staticmethod
    def display_studios(studios):
        print("==================================================================")
        for row in studios:
            print("Id: {0}, name: {1}, country: {2}".format(row[0], row[1], row[2]))
        print("==================================================================")

    @staticmethod
    def display_studio(studio):
        print("==================================================================")
        print("Id: {0}, name: {1}, country: {2}".format(studio["data"][0], studio["data"][1], studio["data"][2]))
        for row in studio["movies"]:
            print("Id: {0}, name: {1}, genre: {2}".format(row[0], row[1], row[3]))
        print("==================================================================")

    @staticmethod
    def display_actors(actors):
        print("==================================================================")
        for row in actors:
            print("Id: {0}, name: {1}, gender: {2}, age: {3}".format(row[0], row[1], row[2], row[3]))
        print("==================================================================")

    @staticmethod
    def display_actor(actor):
        print("==================================================================")
        print("Id: {0}, name: {1}, gender: {2}, age: {3}".format(actor["data"][0], actor["data"][1],
                                                                 actor["data"][2], actor["data"][3]))
        for row in actor["contracts"]:
            print("Movie: {0}, studio: {1}, value: {2}".format(row["movie"], row["studio"], row["value"]))
        print("==================================================================")

    @staticmethod
    def display_movies(movies):
        print("==================================================================")
        for row in movies:
            print("Id: {0}, name: {1}, genre: {2}, budget: {3}".format(row[0], row[1], row[3], row[4]))
            print("Description: {0}".format(row[2]))
        print("==================================================================")

    @staticmethod
    def display_movie(movie):
        print("==================================================================")
        print("Id: {0}, name: {1}, genre: {2}, budget: {3}".format(movie["data"][0], movie["data"][1],
                                                                   movie["data"][3], movie["data"][4]))
        print("Description: {0}".format(movie["data"][2]))
        for row in movie["actors"]:
            print("Id: {0}, name: {1}, gender: {2}, age: {3}".format(row[0], row[1], row[2], row[3]))
        print("==================================================================")

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
