import view
import movie_model


class MovieController(object):

    def __init__(self):
        self.view = view.View()
        self.movie = movie_model.MovieModel()

    def show_movies(self):
        movies = self.movie.get_all_movies()
        if movies:
            self.view.display_movies(movies)

    def show_movie(self):
        print("Input name:")
        name = input()
        if name:
            movie = self.movie.get_movie_by_name(name)
            if movie is None:
                self.view.display_no_results()
            else:
                self.view.display_movie(movie)
        else:
            print("Incorrect input")

    def create_movie(self):
        try:
            print("Input name:")
            name = input()
            print("Input genre:")
            genre = input()
            print("Input description:")
            description = input()
            print("Input budget:")
            budget = int(input())
            if name and genre and description and budget:
                movie = self.movie.create_movie(name, description, genre, budget)
                self.view.display_success()
            else:
                print("Incorrect input")
        except ValueError:
            print("Incorrect input")

    def update_movie(self):
        try:
            print("Input name:")
            name = input()
            print("Input new name:")
            new_name = input()
            print("Input genre:")
            genre = input()
            print("Input description:")
            description = input()
            print("Input budget:")
            budget = int(input())
            if name and genre and description and budget:
                movie = self.movie.update_movie(name, new_name, description, genre, budget)
                if movie:
                    self.view.display_success()
                else:
                    self.view.display_error()
            else:
                print("Incorrect input")
        except ValueError:
            print("Incorrect input")

    def delete_movie(self):
        print("Input name:")
        name = input()
        if not name:
            print("Incorrect input")
        else:
            movie = self.movie.remove_movie(name)
            if movie:
                self.view.display_success()
            else:
                self.view.display_error()

    def delete_actor_from_movie(self):
        try:
            print("Input movie id:")
            movie_id = int(input())
            print("Input actor id:")
            actor_id = int(input())
            movie = self.movie.remove_actor_from_movie(movie_id, actor_id)
            if movie:
                self.view.display_success()
            else:
                self.view.display_error()
        except ValueError:
            print("Incorrect input")

    def add_actor_to_movie(self):
        try:
            print("Input movie id:")
            movie_id = int(input())
            print("Input actor id:")
            actor_id = int(input())
            movie = self.movie.add_actor_to_movie(movie_id, actor_id)
            if movie:
                self.view.display_success()
            else:
                self.view.display_error()
        except ValueError:
            print("Incorrect input")

