from controllers.adminController import AdminController


class AdminView:
    def __init__(self, state):
        self.state = state
        self.adminController = AdminController(state)

    def show(self):
        key = 1
        while key != 0:
            print("1. Journal")
            print("2. Top 10 spammers")
            print("3. Top 10 senders")
            print("0. Quit")
            try:
                key = int(input())
            except ValueError:
                print("Incorrect input")
                key = 4
            if key == 1:
                journal = self.adminController.get_journal()
                print("-----------------------")
                for entry in journal:
                    print(entry)
                print("-----------------------")
            elif key == 2:
                top10 = self.adminController.get_top_10_spammers()
                print("-----------------------")
                for spammer in top10:
                    print(spammer[0], spammer[1])
                print("-----------------------")
            elif key == 3:
                top10 = self.adminController.get_top_10_senders()
                print("-----------------------")
                for sender in top10:
                    print(sender[0], sender[1])
                print("-----------------------")
