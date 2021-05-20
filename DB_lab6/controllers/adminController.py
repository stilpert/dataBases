from models.spammersSortedSet import SpammersSortedSet
from models.sendersSortedSet import SendersSortedSet
from models.JournalList import JournalList


class AdminController:
    def __init__(self, state):
        self.state = state
        self.spammersSortedSet = SpammersSortedSet(state)
        self.sendersSortedSet = SendersSortedSet(state)
        self.journalList = JournalList(state["redis"])

    def get_top_10_spammers(self):
        arr = self.spammersSortedSet.get_all_spammers()
        size = len(arr)
        return arr[(size-10):size]

    def get_top_10_senders(self):
        arr = self.sendersSortedSet.get_all_senders()
        size = len(arr)
        return arr[(size-10):size]

    def get_journal(self):
        return self.journalList.get_all_entries()
