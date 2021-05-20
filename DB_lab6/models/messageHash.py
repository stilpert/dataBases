import redis


class MessageHash:
    def __init__(self, state):
        self.state = state
        self.r = state["redis"]

    def add_message(self, name, message):
        self.r.hset("messages", name, message)

    def get_message(self, name):
        return self.r.hget("messages", name)

    def remove_message(self, name):
        self.r.hdel("messages", name)

    def get_all_messages(self):
        return self.r.hgetall("messages")

    def get_keys(self):
        return self.r.hkeys("messages")


if __name__ == '__main__':
    r = redis.Redis()
    state1 = {'redis': r}
    hash1 = MessageHash(state1)
    # hash1.add_message("Me", "adfsafasdf")
    print(hash1.get_all_messages())
    # hash1.remove_message("Me")
    # print(hash1.get_all_messages())
    print(hash1.get_message('Illiya'))