import threading
import random as rn
import string
import time
from controllers.userController import UserController


class UserEmulator(threading.Thread):
    def __init__(self, state, name):
        threading.Thread.__init__(self)
        self.name = name
        self.redis = state["redis"]
        self.userController = UserController(state, name)

    def run(self):
        names = ['James', 'John', 'Robert', 'Michael', 'William', 'Mary', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth']
        self.userController.login()
        letters = string.ascii_letters
        for i in range(rn.randint(3, 13)):
            msg = ''.join(rn.choice(letters) for i in range(20))
            # print(self.name, msg, names[i-3])
            self.userController.write_message(names[i-3], msg)
            time.sleep(3)
        self.userController.logout()
