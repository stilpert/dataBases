from view import View
from models import Actor, Movie, Studio, Contract
from crud import Session
from sqlalchemy.exc import SQLAlchemyError


class ActorController(object):

    @staticmethod
    def show_actors():
        try:
            s = Session()
            actors = s.query(Actor).all()
            s.close()
            if actors:
                View.display_actors(actors)
            else:
                View.display_no_results()
        except SQLAlchemyError:
            View.display_error()

    @staticmethod
    def show_actor():
        try:
            print("Input name:")
            name = input()
            if name:
                s = Session()
                actor = s.query(Actor).filter_by(full_name=name).first()
                s.close()
                if actor is None:
                    View.display_no_results()
                else:
                    View.display_actor(actor)
            else:
                print("Incorrect input")
        except SQLAlchemyError:
            View.display_error()

    @staticmethod
    def create_actor():
        try:
            print("Input name:")
            name = input()
            print("Input gender:")
            gender = input()
            print("Input age:")
            age = int(input())
            if name and gender and age:
                s = Session()
                s.add(Actor(
                    full_name=name,
                    gender=gender,
                    age=age,
                ))
                s.commit()
                s.close()
                View.display_success()
            else:
                print("Incorrect input")
        except SQLAlchemyError:
            View.display_error()
        except ValueError:
            print("Incorrect input")

    @staticmethod
    def update_actor():
        try:
            print("Input name:")
            name = input()
            print("Input new name:")
            new_name = input()
            print("Input gender:")
            gender = input()
            print("Input age:")
            age = int(input())
            if name and (new_name or gender or age):
                s = Session()
                actor = s.query(Actor).filter_by(full_name=name).first()
                if new_name:
                    actor.full_name = new_name
                if gender:
                    actor.gender = gender
                if age:
                    actor.age = age
                s.add(actor)
                s.commit()
                s.close()
                View.display_success()
            else:
                print("Incorrect input")
        except SQLAlchemyError:
            View.display_error()
        except ValueError:
            print("Incorrect input")

    @staticmethod
    def delete_actor():
        print("Input name:")
        name = input()
        if not name:
            print("Incorrect input")
        else:
            try:
                s = Session()
                s.query(Actor).filter_by(full_name=name).delete()
                s.commit()
                s.close()
                View.display_success()

            except SQLAlchemyError:
                View.display_error()

    @staticmethod
    def add_contract_to_actor():
        try:
            print("Input movie name:")
            movie_name = input()
            print("Input actor name:")
            actor_name = input()
            print("Input studio name:")
            studio_name = input()
            print("Input value:")
            value = int(input())
            if movie_name and actor_name and studio_name and value:
                s = Session()
                movie = s.query(Movie).filter_by(name=movie_name).first()
                studio = s.query(Studio).filter_by(name=studio_name).first()
                actor = s.query(Actor).filter_by(full_name=actor_name).first()
                if (movie is None) or (actor is None) or (studio is None):
                    View.display_no_results()
                    s.close()
                else:
                    s.add(Contract(
                        movie_id=movie.id,
                        studio_id=studio.id,
                        actor_id=actor.id,
                        value=value
                    ))
                    s.commit()
                    s.close()
                    View.display_success()
            else:
                print("Incorrect input")
        except SQLAlchemyError as e:
            View.display_error()

    @staticmethod
    def delete_contract_from_actor():
        try:
            print("Input movie name:")
            movie_name = input()
            print("Input actor name:")
            actor_name = input()
            print("Input studio name:")
            studio_name = input()

            if movie_name and actor_name and studio_name:
                s = Session()
                movie = s.query(Movie).filter_by(name=movie_name).first()
                studio = s.query(Studio).filter_by(name=studio_name).first()
                actor = s.query(Actor).filter_by(full_name=actor_name).first()
                if (movie is None) or (actor is None) or (studio is None):
                    View.display_no_results()
                    s.close()
                else:
                    s.query(Contract).filter(Contract.movie_id == movie.id,
                                             Contract.actor_id == actor.id, Contract.studio_id == studio.id).delete()

                    s.commit()
                    s.close()
                    View.display_success()
            else:
                print("Incorrect input")
        except SQLAlchemyError as e:
            print(e)
            View.display_error()


if __name__ == '__main__':

    ActorController.delete_actor()
