import redis
from views.userView import UserView
from views.workerView import WorkerView
from views.adminView import AdminView
from controllers.userController import UserController



class LoginView:
    def __init__(self, state):
        self.state = state

    def show(self):
        key = 1
        while key != 0:
            print("1. Login as user")
            print("2. Login as admin")
            print("3. login as worker")
            print("0. Quit")
            try:
                key = int(input())
            except ValueError:
                print("Incorrect input")
                key = 4
            if key == 1:
                print("1. Input your name: ")
                name = input()
                UserController(self.state, name).login()
                UserView(self.state, name).show()
            elif key == 2:
                AdminView(self.state).show()
            elif key == 3:
                WorkerView(self.state).show()





