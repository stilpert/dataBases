from controller import Controller


class View:
    def __init__(self, state):
        self.state = state
        self.controller = Controller(state)

    def show(self):
        key = 1
        while key != 0:
            print("1. Run scrappers")
            print("2. Get charts")
            print("3. Get map")
            print("4. Get statistic")
            print("5. Get Hotel by name")
            print("0. Quit")
            try:
                key = int(input())
            except ValueError:
                print("Incorrect input")
                key = 10
            if key == 1:
                print("1. Run Karpaty booking scrapper")
                print("2. Run Karpaty info scrapper")
                try:
                    key = int(input())
                except ValueError:
                    print("Incorrect input")
                    key = 5
                if key == 1:
                    self.controller.run_booking_scrapper()
                elif key == 2:
                    self.controller.run_info_scrapper()
            elif key == 2:
                self.controller.get_chart_data()
            elif key == 3:
                self.controller.get_map()
            elif key == 4:
                self.controller.get_statistic()
            elif key == 5:
                print("Input name")
                name = input()
                hotel = self.controller.get_hotel_by_name(name)
                if not hotel:
                    print("There isn't hotel with name", name)
                else:
                    print("Name:", hotel['name'])
                    print("Resort:", hotel['resort'])
                    print("Location:", hotel['location'])
                    print("Price:", hotel['price'])
                    print("Description:", hotel['desc'])





