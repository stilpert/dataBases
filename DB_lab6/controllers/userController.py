import redis
from models.userSet import UserSet
from models.userOnlineSet import UserOnlineSet
from models.messageHash import MessageHash
from models.userMessageSortedSet import UserMessageSortedSet
from models.sentMessagesList import SentMessagesList
from models.sendersSortedSet import SendersSortedSet
import json


class UserController:
    def __init__(self, state, name):
        self.state = state
        self.redis = state["redis"]
        self.name = name
        self.userSet = UserSet(state)
        self.userOnlineSet = UserOnlineSet(state)
        self.messageHash = MessageHash(state)
        self.userMessageSortedSet = UserMessageSortedSet(state)
        self.sentMessageList = SentMessagesList(state)
        self.sendersSortedSet = SendersSortedSet(state)

    def login(self):
        self.userSet.add_user(self.name)
        self.userOnlineSet.add_user(self.name)
        self.redis.publish('journal', 'Login: ' + self.name)

    def logout(self):
        self.userOnlineSet.remove_user(self.name)
        self.redis.publish('journal', 'Logout: ' + self.name)

    def get_statistic(self):
        return {
            'Created': self.userMessageSortedSet.get_messages_count_by_status(self.name, 1),
            'In queue': self.userMessageSortedSet.get_messages_count_by_status(self.name, 2),
            'Checked for spam': self.userMessageSortedSet.get_messages_count_by_status(self.name, 3),
            'Banned as spam': self.userMessageSortedSet.get_messages_count_by_status(self.name, 4),
            'Sent to recipient': self.userMessageSortedSet.get_messages_count_by_status(self.name, 5),
            'Delivered': self.userMessageSortedSet.get_messages_count_by_status(self.name, 6),
        }

    def get_messages(self):
        return self.sentMessageList.get_all_messages(self.name)

    def write_message(self, rcp_name, message):
        dict = {
            "recipient": rcp_name,
            "message": message
        }
        self.userMessageSortedSet.add_message(self.name, json.dumps(dict), 1)
        self.messageHash.add_message(self.name, json.dumps(dict))
        res = self.sendersSortedSet.add_sender(self.name)
        if res != 1:
            self.sendersSortedSet.increment_sender_count(self.name)
        self.userMessageSortedSet.update_message(self.name, json.dumps(dict), 2)


if __name__ == '__main__':
    r = redis.Redis()


