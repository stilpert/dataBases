import redis


class JournalList:
    def __init__(self, redis):
        self.r = redis

    def add_entry(self, message):
        self.r.lpush('journal', message)

    def get_all_entries(self):
        return self.r.lrange('journal', 0, 100)
