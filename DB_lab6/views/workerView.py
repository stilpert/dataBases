from controllers.workerController import WorkerController


class WorkerView:
    def __init__(self, state):
        self.state = state
        self.workerController = WorkerController(state)

    def show(self):
        key = 1
        while key != 0:
            print("1. Get messages queue")
            print("2. Set message status")
            print("0. Logout")
            try:
                key = int(input())
            except ValueError:
                print("Incorrect input")
                key = 4
            if key == 1:
                queue = self.workerController.get_queue()
                print("-----------------------")
                for rcp in queue:
                    print(rcp, queue[rcp])
                print("-----------------------")
            if key == 2:
                print("input sender name:")
                name = input()
                message = self.workerController.get_message(name)
                if message is None:
                    print("There's no message")
                    continue
                print("Message: ")
                print(message)
                print("Input status: \n1. Spam \n2. Not spam. \n0. Close")
                try:
                    status = int(input())
                except ValueError:
                    print("Incorrect input")
                    status = 4
                if status == 1:
                    self.workerController.set_message_status(name, message, 4)
                if status == 2:
                    self.workerController.set_message_status(name, message, 5)
