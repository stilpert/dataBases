from crud import Session
from sqlalchemy.exc import SQLAlchemyError
from view import View
from models import Movie, Actor, casts


class MovieController(object):

    @staticmethod
    def show_movies():
        try:
            s = Session()
            movies = s.query(Movie).all()
            s.close()
            if movies:
                View.display_movies(movies)
            else:
                View.display_no_results()
        except SQLAlchemyError:
            View.display_error()

    @staticmethod
    def show_movie():
        try:
            print("Input name:")
            name = input()
            if name:
                s = Session()
                movie = s.query(Movie).filter_by(name=name).first()
                s.close()
                if movie is None:
                    View.display_no_results()
                else:
                    View.display_movie(movie)
                    View.display_actors(movie.cast)
            else:
                print("Incorrect input")
        except SQLAlchemyError:
            View.display_error()

    @staticmethod
    def create_movie():
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
                s = Session()
                s.add(Movie(
                    name=name,
                    genre=genre,
                    description=description,
                    budget=budget
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
    def update_movie():
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
            if name and (new_name or genre or description or budget):
                s = Session()
                movie = s.query(Movie).filter_by(name=name).first()
                if new_name:
                    movie.name = new_name
                if genre:
                    movie.genre = genre
                if description:
                    movie.description = description
                if budget:
                    movie.budget = budget
                s.add(movie)
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
    def delete_movie():
        print("Input name:")
        name = input()
        if not name:
            print("Incorrect input")
        else:
            try:
                s = Session()
                s.query(Movie).filter_by(name=name).delete()
                s.commit()
                s.close()
                View.display_success()
            except SQLAlchemyError:
                View.display_error()

    @staticmethod
    def add_actor_to_movie():
        try:
            print("Input movie name:")
            movie_name = input()
            print("Input actor name:")
            actor_name = input()
            if movie_name and actor_name:
                s = Session()
                movie = s.query(Movie).filter_by(name=movie_name).first()
                actor = s.query(Actor).filter_by(full_name=actor_name).first()
                s.add(movie)
                if (movie is None) or (actor is None):
                    View.display_no_results()
                    s.close()
                else:
                    movie.cast.append(actor)
                    View.display_success()
                    s.commit()
                    s.close()
            else:
                print("Incorrect input")
        except SQLAlchemyError as e:
            View.display_error()

    @staticmethod
    def delete_actor_from_movie():
        try:
            print("Input movie name:")
            movie_name = input()
            print("Input actor name:")
            actor_name = input()
            if movie_name and actor_name:
                s = Session()
                movie = s.query(Movie).filter_by(name=movie_name).first()
                actor = s.query(Actor).filter_by(full_name=actor_name).first()
                s.add(movie)
                if (movie is None) or (actor is None):
                    View.display_no_results()
                    s.close()
                else:
                    movie.cast.remove(actor)
                    View.display_success()
                    s.commit()
                    s.close()
            else:
                print("Incorrect input")
        except (SQLAlchemyError, Exception) as e:
            print(e)
            View.display_error()


if __name__ == '__main__':

    s = Session()
    actor = s.query(Movie).filter_by(name="The Avengers").first()
    s.close()
