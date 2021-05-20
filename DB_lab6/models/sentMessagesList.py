import redis


class SentMessagesList:
    def __init__(self, state):
        self.state = state
        self.r = state["redis"]

    def add_message(self, name, message):
        self.r.lpush(name + "_sent", message)

    def get_all_messages(self, name):
        return self.r.lrange(name + "_sent", 0, 100)
