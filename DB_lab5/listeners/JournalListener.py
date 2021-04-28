import redis
import threading
from models.JournalList import JournalList


class JournalListener(threading.Thread):
    def __init__(self, r, channels):
        threading.Thread.__init__(self)
        self.redis = r
        self.pubsub = self.redis.pubsub()
        self.pubsub.subscribe(channels)
        self.journalList = JournalList(r)

    def run(self):
        for item in self.pubsub.listen():
            if item != "1":
                self.journalList.add_entry(item['data'])
