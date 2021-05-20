from model import Hotel
import numpy as np
import pandas as pd
from carpathiansRental.run_info_spider import InfoScrapperRunner
from carpathiansRental.run_booking_spider import BookingScrapperRunner
import matplotlib.pyplot as plt
import folium
from matplotlib import colors
from collections import Counter


class Controller:
    def __init__(self, state):
        self.state = state
        self.model = Hotel(state)
        self.set = pd.DataFrame(self.model.get_all_hotels())
        pd.set_option('display.max_rows', 10)

    def get_hotel_by_name(self, name):
        return self.model.get_hotel(name)

    def get_chart_data(self):
        self.get_pie_chart()
        self.get_price_means_chart()
        self.get_price_modes_chart()

    def get_statistic(self):
        print(self.set)
        print("Resort count: ")
        print(self.set['resort'].value_counts(ascending=True))
        print("Correlation between price and distance")
        print(self.set[['price', 'distance']].corr(method='pearson'))

    def get_map(self):
        resorts = np.unique(self.set['resort'])
        color_dict = dict(zip(resorts, list(colors.cnames.values())[0:-1:len(resorts)]))

        map_resorts = folium.Map(location=[self.set['latitude'].mean(), self.set['longitude'].mean()], zoom_start=9)
        obs = list(zip(self.set['latitude'], self.set['longitude'], self.set['resort']))

        for el in obs[0:-1]:
            folium.CircleMarker(el[0:2], color=color_dict[el[2]], fill_color=el[2], radius=10).add_to(map_resorts)

        map_resorts.save("./charts/map.html")

    def get_price_means_chart(self):
        values_mean = []
        resorts = self.set.resort.unique()
        for r in resorts:
            values_mean.append(int(self.set[self.set['resort'] == r].price.mean()))
        x = np.arange(len(resorts))
        width = 0.6
        fig, ax = plt.subplots()
        rects1 = ax.bar(x, values_mean, width, label=' ')
        ax.set_ylabel('Price')
        ax.set_title('Resorts price means')
        ax.set_xticks(x)
        ax.set_xticklabels(resorts)
        ax.legend()
        ax.bar_label(rects1, padding=3)
        fig.tight_layout()
        plt.savefig("./charts/chart_mean.png")

    def get_price_modes_chart(self):
        values_mode = []
        resorts = self.set.resort.unique()
        for r in resorts:
            values_mode.append(int(self.set[self.set['resort'] == r].price.mode()))
        x = np.arange(len(resorts))
        width = 0.6
        fig, ax = plt.subplots()
        rects1 = ax.bar(x, values_mode, width, label=' ')
        ax.set_ylabel('Price')
        ax.set_title('Resorts price mode')
        ax.set_xticks(x)
        ax.set_xticklabels(resorts)
        ax.legend()
        ax.bar_label(rects1, padding=3)
        fig.tight_layout()
        plt.savefig("./charts/chart_mode.png")

    def get_pie_chart(self):
        dict1 = dict(self.set['resort'].value_counts(ascending=True))
        labels = dict1.keys()
        values = dict1.values()
        explode = (0, 0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
        fig1, ax1 = plt.subplots()
        ax1.pie(values, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.savefig('./charts/pie-chart.png')

    def run_booking_scrapper(self):
        client = BookingScrapperRunner()
        client.start()

    def run_info_scrapper(self):
        client = InfoScrapperRunner()
        client.start()

