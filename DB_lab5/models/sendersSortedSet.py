import redis


class SendersSortedSet:
    def __init__(self, state):
        self.state = state
        self.r = state["redis"]

    def add_sender(self, name):
        return self.r.zadd("senders", {name: 1.0}, nx=True)

    def increment_sender_count(self, name):
        self.r.zincrby("senders", 1, name)

    def get_all_senders(self):
        return self.r.zrangebyscore("senders", 0, 100, withscores=True)


if __name__ == '__main__':
    r = redis.Redis()
    state1 = {'redis': r}
    set1 = SendersSortedSet(state1)
    set1.add_sender("Tom")
    print(set1.get_all_senders())
    res = set1.add_sender("Tom")
    if res != 1:
        set1.increment_sender_count("Tom")
    print(set1.get_all_senders())
    # set1.increment_sender_count("Dmitriy")
