import threading
import random as rn
import string
import time
from controllers.workerController import WorkerController


class WorkerEmulator(threading.Thread):
    def __init__(self, state):
        threading.Thread.__init__(self)
        self.redis = state["redis"]
        self.workerController = WorkerController(state)

    def run(self):
        while True:
            data = self.workerController.get_one_pair()
            if data is not None:
                if bool(rn.getrandbits(1)):
                    self.workerController.set_message_status(str(data[0]), str(data[1]), 4)
                else:
                    self.workerController.set_message_status(str(data[0]), str(data[1]), 5)
                time.sleep(1)
