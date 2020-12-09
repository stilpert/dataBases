import dataset_beckend


class ActorModel(object):

    def __init__(self):
        self._connection = dataset_beckend.connect_to_bd()

    def get_all_actors(self):
        return dataset_beckend.select_all(self._connection, "actors")

    def get_actor_by_name(self, name):
        actor = dataset_beckend.select_by_pr(self._connection, "full_name", name, "actors")[0]
        contracts_id = dataset_beckend.select_by_pr(self._connection, "actor_id", actor[0], "contracts")
        contracts = []
        for contract in contracts_id:
            studio = dataset_beckend.select_by_pr(self._connection, "id", contract[3], "studios")[0][1]
            movie = dataset_beckend.select_by_pr(self._connection, "id", contract[1], "movies")[0][1]
            contracts.append({"movie": movie, "studio": studio, "value": contract[4]})
        return {"data": actor, "contracts": contracts}

    def create_actor(self, name, gender, age):
        return dataset_beckend.insert_one(self._connection, {'full_name': name,
                                                             'gender': gender,
                                                             'gender': gender,
                                                             'age': age}, "actors")

    def update_actor(self, name, new_name, gender, age):
        return dataset_beckend.update_one(self._connection, {'full_name': new_name,
                                                             'gender': gender,
                                                             'gender': gender,
                                                             'age': age}, "full_name", name, "actors")

    def remove_actor(self, name):
        actor_id = dataset_beckend.select_by_pr(self._connection, "full_name", name, "actors")[0][0]
        dataset_beckend.delete_items(self._connection, 'actor_id', actor_id, "contracts")
        dataset_beckend.delete_items(self._connection, 'full_name', name, "actors")

    def add_contract_to_actor(self, actor_id, studio_id, movie_id, value):
        return dataset_beckend.insert_one(self._connection, {'actor_id': actor_id,
                                                             'studio_id': studio_id,
                                                             'movie_id': movie_id,
                                                             'value': value}, "contracts")

    def remove_contract_from_actor(self, actor_id, studio_id, movie_id):
        return dataset_beckend.delete_items_by_couple_prs(self._connection, {'actor_id': actor_id,
                                                                             'movie_id': movie_id,
                                                                             'studio_id': studio_id}, "contracts")

    def generate_random_actors(self, number):
        return dataset_beckend.generate_items(self._connection, number, "actors")


if __name__ == '__main__':
    model = ActorModel()
    for row in model.get_all_actors():
        print(row[0], row[1], row[2])
