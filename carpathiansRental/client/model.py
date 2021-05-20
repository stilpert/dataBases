import pymongo


class Hotel:
    def __init__(self, state):
        self.state = state
        self.db = state["db"]
        self.collection = self.db["hotels"]

    def get_hotel(self, name):
        return self.collection.find_one({"name": name})

    def get_all_hotels(self):
        return self.collection.find({}, {"_id": 0, "desc": 0, "location": 0})
