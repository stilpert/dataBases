import dataset_beckend


class MovieModel(object):

    def __init__(self):
        self._connection = dataset_beckend.connect_to_bd()

    def get_all_movies(self):
        return dataset_beckend.select_all(self._connection, "movies")

    def get_movie_by_name(self, name):
        movie = dataset_beckend.select_by_pr(self._connection, "name", name, "movies")[0]
        casts = dataset_beckend.select_by_pr(self._connection, "movie_id", movie[0], "casts")
        actors = []
        for cast in casts:
            actors.append(dataset_beckend.select_by_pr(self._connection, "id", cast[2], "actors")[0])
        return {"data": movie, "actors": actors}

    def create_movie(self, name, description, genre, budget):
        return dataset_beckend.insert_one(self._connection, {'name': name,
                                                             'description': description,
                                                             'genre': genre,
                                                             'budget': budget}, "movies")

    def update_movie(self, name, new_name, description, genre, budget):
        return dataset_beckend.update_one(self._connection, {'name': new_name,
                                                             'description': description,
                                                             'genre': genre,
                                                             'budget': budget}, "name", name, "movies")

    def remove_movie(self, name):
        movie_id = dataset_beckend.select_by_pr(self._connection, "name", name, "movies")[0][0]
        dataset_beckend.delete_items(self._connection, 'movie_id', movie_id, "casts")
        dataset_beckend.delete_items(self._connection, 'name', name, "movies")

    def add_actor_to_movie(self, movie_id, actor_id):
        return dataset_beckend.insert_one(self._connection, {'movie_id': movie_id, 'actor_id': actor_id}, "casts")

    def remove_actor_from_movie(self, movie_id, actor_id):
        return dataset_beckend.delete_items_by_couple_prs(self._connection, {'movie_id': movie_id,
                                                                             'actor_id': actor_id}, "casts")


if __name__ == '__main__':
    model = MovieModel()
    for row in model.get_all_movies():
        print(row[0], row[1], row[2])
