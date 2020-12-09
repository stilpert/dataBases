import dataset_beckend


class StudioModel(object):

    def __init__(self):
        self._connection = dataset_beckend.connect_to_bd()

    def get_all_studios(self):
        return dataset_beckend.select_all(self._connection, "studios")

    def get_studio_by_name(self, name):
        try:
            studio = dataset_beckend.select_by_pr(self._connection, "name", name, "studios")[0]
            movies_id = dataset_beckend.select_by_pr(self._connection, "studio_id", studio[0], "creators")
            movies = []
            for m_id in movies_id:
                movies.append(dataset_beckend.select_by_pr(self._connection, "id", m_id[1], "movies")[0])
            studio = {"data": studio, "movies": movies}

        except IndexError:
            studio = None
        finally:
            return studio

    def create_studio(self, name, country):
        return dataset_beckend.insert_one(self._connection, {'name': name, 'country': country}, "studios")

    def update_studio(self, name, new_name, country):
        return dataset_beckend.update_one(self._connection, {'name': new_name, 'country': country},
                                          "name", name, "studios")

    def remove_studio(self, name):
        studio_id = dataset_beckend.select_by_pr(self._connection, "name", name, "studios")[0][0]
        dataset_beckend.delete_items(self._connection, 'studio_id', studio_id, "creators")
        dataset_beckend.delete_items(self._connection, 'name', name, "studios")

    def add_movie_to_studio(self, movie_id, studio_id):
        return dataset_beckend.insert_one(self._connection, {'movie_id': movie_id, 'studio_id': studio_id}, "creators")

    def remove_movie_from_studio(self, movie_id, studio_id):
        return dataset_beckend.delete_items_by_couple_prs(self._connection, {'movie_id': movie_id,
                                                                             'studio_id': studio_id}, "creators")


if __name__ == '__main__':
    model = StudioModel()
    for row in model.get_all_studios():
        print(row[0], row[1], row[2])








