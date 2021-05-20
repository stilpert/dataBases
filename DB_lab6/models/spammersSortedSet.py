import redis


class SpammersSortedSet:
    def __init__(self, state):
        self.state = state
        self.r = state["redis"]

    def add_spammer(self, name):
        return self.r.zadd("spammers", {name: 1.0}, nx=True)

    def increment_spammer_count(self, name):
        self.r.zincrby("spammers", 1, name)

    def get_all_spammers(self):
        return self.r.zrangebyscore("spammers", 0, 100, withscores=True)


if __name__ == '__main__':
    r = redis.Redis()
    state1 = {'redis': r}
    set1 = SpammersSortedSet(state1)
    # set1.add_spammer('Karina')
    print(set1.get_all_spammers())
    set1.increment_spammer_count("Dmitriy")
    print(set1.get_all_spammers())

