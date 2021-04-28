import json
from json import JSONDecodeError
from models.messageHash import MessageHash
from models.userMessageSortedSet import UserMessageSortedSet
from models.sentMessagesList import SentMessagesList
from models.spammersSortedSet import SpammersSortedSet


class WorkerController:
    def __init__(self, state):
        self.state = state
        self.redis = state["redis"]
        self.messageHash = MessageHash(state)
        self.userMessageSortedSet = UserMessageSortedSet(state)
        self.sentMessageList = SentMessagesList(state)
        self.spammersSortedSet = SpammersSortedSet(state)

    def get_message(self, name):
        message = self.messageHash.get_message(name)
        self.userMessageSortedSet.update_message(name, message, 3)
        return message

    def get_one_pair(self):
        keys = self.messageHash.get_keys()
        if len(keys) == 0:
            return
        key = keys[0]
        message = self.messageHash.get_message(key)
        self.messageHash.remove_message(key)
        return key, message

    def set_message_status(self, name, message, status):
        # try:
        self.userMessageSortedSet.update_message(name, message, status)

        self.messageHash.remove_message(name)
        if status == 5:
            try:
                dict = json.loads(message)
            except JSONDecodeError:
                return
            self.sentMessageList.add_message(dict['recipient'], name + ": " + dict['message'])
            self.userMessageSortedSet.update_message(name, message, 6)
        elif status == 4:
            self.redis.publish('journal', 'Spam in message of ' + name)
            res = self.spammersSortedSet.add_spammer(name)
            if res != 1:
                self.spammersSortedSet.increment_spammer_count(name)
        # except Exception:
        #     return

    def get_queue(self):
        return self.messageHash.get_all_messages()

