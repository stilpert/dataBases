import view
import actors_model


class ActorController(object):

    def __init__(self):
        self.view = view.View()

        self.actor = actors_model.ActorModel()
    
    def show_actors(self):
        actors = self.actor.get_all_actors()
        if actors:
            self.view.display_actors(actors)

    def show_actor(self):
        print("Input name:")
        name = input()
        if name:
            actor = self.actor.get_actor_by_name(name)
            if actor is None:
                self.view.display_no_results()
            else:
                self.view.display_actor(actor)
        else:
            print("Incorrect input")

    def create_actor(self):
        try:
            print("Input name:")
            name = input()
            print("Input gender:")
            gender = input()
            print("Input age:")
            age = int(input())
            if name and gender and age:
                actor = self.actor.create_actor(name, gender, age)
                self.view.display_success()
            else:
                print("Incorrect input")
        except ValueError:
            print("Incorrect input")

    def update_actor(self):
        try:
            print("Input name:")
            name = input()
            print("Input new name:")
            new_name = input()
            print("Input gender:")
            gender = input()
            print("Input age:")
            age = int(input())
            if name and new_name and gender and age:
                actor = self.actor.update_actor(name, new_name, gender, age)
                if actor:
                    self.view.display_success()
                else:
                    self.view.display_error()
            else:
                print("Incorrect input")
        except ValueError:
            print("Incorrect input")

    def delete_actor(self):
        print("Input name:")
        name = input()
        if not name:
            print("Incorrect input")
        else:
            actor = self.actor.remove_actor(name)
            if actor:
                self.view.display_success()
            else:
                self.view.display_error()

    def delete_contract_from_actor(self):
        try:
            print("Input actor id:")
            actor_id = int(input())
            print("Input studio id:")
            studio_id = int(input())
            print("Input movie id:")
            movie_id = int(input())
            actor = self.actor.remove_contract_from_actor(actor_id, studio_id, movie_id)
            if actor:
                self.view.display_success()
            else:
                self.view.display_error()
        except ValueError:
            print("Incorrect input")

    def add_contract_to_actor(self):
        try:
            print("Input actor id:")
            actor_id = int(input())
            print("Input studio id:")
            studio_id = int(input())
            print("Input movie id:")
            movie_id = int(input())
            actor = self.actor.add_contract_to_actor(actor_id, studio_id, movie_id)
            if actor:
                self.view.display_success()
            else:
                self.view.display_error()
        except ValueError:
            print("Incorrect input")

    def generate_random_actors(self):
        try:
            print("Input actors number:")
            num = int(input())
            actors = self.actor.generate_random_actors(num)
            if actors:
                self.view.display_actors(actors)
            else:
                self.view.display_no_results()
        except ValueError:
            print("Incorrect input")
