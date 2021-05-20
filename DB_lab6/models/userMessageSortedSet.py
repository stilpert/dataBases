import redis


class UserMessageSortedSet:
    def __init__(self, state):
        self.state = state
        self.r = state["redis"]

    def add_message(self, name, message, status):
        self.r.zadd(name, {message: float(status)})

    def update_message(self, name, message, status):
        self.r.zadd(name, {message: float(status)})

    def get_messages_count_by_status(self, name, status):
        return self.r.zcount(name, status, status)

    def get_all_messages(self, name):
        return self.r.zrangebyscore(name, 0, 6, withscores=True)


if __name__ == '__main__':
    r = redis.Redis()
    state1 = {'redis': r}
    set = UserMessageSortedSet(state1)
    set.add_message("Illiya", "fasdfasdf", 6)
    print(set.get_all_messages("Illiya"))
    print(set.get_messages_count_by_status("Illiya", 6))
    set.update_message("Illiya", "fasdfasdf", 5)
    print(set.get_all_messages("Illiya"))
    print(set.get_messages_count_by_status("Illiya", 5))
    # print(set.get_message('Illiya'))