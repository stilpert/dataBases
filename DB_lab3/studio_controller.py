from view import View
from models import Studio, Movie, creators
from crud import Session
from sqlalchemy.exc import SQLAlchemyError


class StudioController(object):

    @staticmethod
    def show_studios():
        try:
            s = Session()
            studios = s.query(Studio).all()
            s.close()
            if studios:
                View.display_studios(studios)
            else:
                View.display_no_results()
        except SQLAlchemyError:
            View.display_error()

    @staticmethod
    def show_studio():
        try:
            print("Input name:")
            name = input()
            if name:
                s = Session()
                studio = s.query(Studio).filter_by(name=name).first()
                s.close()
                if studio is None:
                    View.display_no_results()
                else:
                    View.display_studio(studio)
                    View.display_movies(studio.movies)
            else:
                print("Incorrect input")
        except SQLAlchemyError:
            View.display_error()

    @staticmethod
    def create_studio():
        try:
            print("Input name:")
            name = input()
            print("Input country:")
            country = input()
            if name and country:
                s = Session()
                s.add(Studio(
                    name=name,
                    country=country
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
    def update_studio():
        try:
            print("Input name:")
            name = input()
            print("Input new name:")
            new_name = input()
            print("Input country:")
            country = input()
            if name and (new_name or country):
                s = Session()
                studio = s.query(Studio).filter_by(name=name).first()
                if new_name:
                    studio.name = new_name
                if country:
                    studio.country = country
                s.add(studio)
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
    def delete_studio():
        print("Input name:")
        name = input()
        if not name:
            print("Incorrect input")
        else:
            try:
                s = Session()
                s.query(Studio).filter_by(name=name).delete()
                s.commit()
                s.close()
                View.display_success()
            except SQLAlchemyError:
                View.display_error()

    @staticmethod
    def add_movie_to_studio():
        try:
            print("Input movie name:")
            movie_name = input()
            print("Input studio name:")
            studio_name = input()
            if movie_name and studio_name:
                s = Session()
                movie = s.query(Movie).filter_by(name=movie_name).first()
                studio = s.query(Studio).filter_by(name=studio_name).first()
                s.add(studio)
                if (movie is None) or (studio is None):
                    View.display_no_results()
                    s.close()
                else:
                    studio.movies.append(movie)
                    View.display_success()
                    s.commit()
                    s.close()
            else:
                print("Incorrect input")
        except SQLAlchemyError as e:
            View.display_error()

    @staticmethod
    def remove_movie_from_studio():
        try:
            print("Input movie name:")
            movie_name = input()
            print("Input studio name:")
            studio_name = input()
            if movie_name and studio_name:
                s = Session()
                movie = s.query(Movie).filter_by(name=movie_name).first()
                studio = s.query(Studio).filter_by(name=studio_name).first()
                s.add(studio)
                if (movie is None) or (studio is None):
                    View.display_no_results()
                    s.close()
                else:
                    studio.movies.remove(movie)
                    View.display_success()
                    s.commit()
                    s.close()
            else:
                print("Incorrect input")
        except SQLAlchemyError as e:
            View.display_error()

if __name__ == '__main__':

    s = Session()
    actor = s.query(Studio).filter_by(name="The Avengers").first()
    s.close()
