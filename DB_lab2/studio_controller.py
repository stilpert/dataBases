import view
import studio_model


class StudioController(object):

    def __init__(self):
        self.view = view.View()
        self.studio = studio_model.StudioModel()

    def show_studios(self):
        studios = self.studio.get_all_studios()
        if studios:
            self.view.display_studios(studios)

    def show_studio(self):
        print("Input name:")
        name = input()
        if name:
            studio = self.studio.get_studio_by_name(name)
            if studio is None:
                self.view.display_no_results()
            else:
                self.view.display_studio(studio)
        else:
            print("Incorrect input")

    def create_studio(self):
        print("Input name:")
        name = input()
        print("Input country:")
        country = input()
        if name and country:
            studio = self.studio.create_studio(name, country)
            self.view.display_success()
        else:
            print("Incorrect input")

    def update_studio(self):
        print("Input name:")
        name = input()
        print("Input new name:")
        new_name = input()
        print("Input country:")
        country = input()
        if not name or not new_name or not country:
            print("Incorrect input")
        else:
            studio = self.studio.update_studio(name, new_name, country)
            if studio:
                self.view.display_success()
            else:
                self.view.display_error()

    def delete_studio(self):
        print("Input name:")
        name = input()
        if not name:
            print("Incorrect input")
        else:
            studio = self.studio.delete_studio(name)
            if studio:
                self.view.display_success()
            else:
                self.view.display_error()

    def delete_movie_from_studio(self):
        try:
            print("Input movie id:")
            movie_id = int(input())
            print("Input studio id:")
            studio_id = int(input())
            studio = self.studio.remove_movie_from_studio(movie_id, studio_id)
            if studio:
                self.view.display_success()
            else:
                self.view.display_error()
        except ValueError:
            print("Incorrect input")

    def add_movie_to_studio(self):
        try:
            print("Input movie id:")
            movie_id = int(input())
            print("Input studio id:")
            studio_id = int(input())
            studio = self.studio.add_movie_to_studio(movie_id, studio_id)
            if studio:
                self.view.display_success()
            else:
                self.view.display_error()
        except ValueError:
            print("Incorrect input")
