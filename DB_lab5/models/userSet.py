import redis


class UserSet:
    def __init__(self, state):
        self.state = state
        self.r = state["redis"]

    def add_user(self, name):
        self.r.sadd('users', name)

    def remove_user(self, name):
        self.r.srem('users', name)

    def get_all_users(self):
        return self.r.smembers('users')


if __name__ == '__main__':
    r = redis.Redis()
    state1 = {'redis': r}
    userSet = UserSet(state1)
    userSet.add_user("Nick")
    userSet.add_user("Bob")
    print(userSet.get_all_users())
    userSet.remove_user("Nick")
    userSet.remove_user("Bob")
    print(userSet.get_all_users())

