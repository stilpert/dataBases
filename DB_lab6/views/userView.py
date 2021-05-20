import redis
from controllers.userController import UserController


class UserView:
    def __init__(self, state, name):
        self.state = state
        self.name = name
        self.userController = UserController(state, name)

    def show(self):
        key = 1
        while key != 0:
            print("1. Check messages")
            print("2. Write message")
            print("3. Get statistic")
            print("0. Logout")
            try:
                key = int(input())
            except ValueError:
                print("Incorrect input")
                key = 4
            if key == 1:
                print("-----------------------")
                for msg in self.userController.get_messages():
                    print(msg)
                print("-----------------------")
            elif key == 2:
                print("Input name of recipient: ")
                name = input()
                print("Input message: ")
                message = input()
                self.userController.write_message(name, message)
            elif key == 3:
                dictionary = self.userController.get_statistic()
                for status in dictionary:
                    print(status + ": " + str(dictionary[status]))
            elif key == 0:
                self.userController.logout()

