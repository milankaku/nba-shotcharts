import requests
import pandas
import matplotlib.pyplot as plt
import seaborn

headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}


class ShotData(object):

    def __init__(self):
        self.url = 'http://stats.nba.com/stats/shotchartdetail?CFID=33&CFPAR'\
                'AMS=2016-17&ContextFilter=&ContextMeasure=FGA&DateFrom=&D'\
                'ateTo=&GameID=&GameSegment=&LastNGames=0&LeagueID=00&Loca'\
                'tion=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&'\
                'PaceAdjust=N&PerMode=PerGame&Period=0&PlayerID=202710&Plu'\
                'sMinus=N&PlayerPosition=&Rank=N&RookieYear=&Season=2016-17&Seas'\
                'onSegment=&SeasonType=Regular+Season&TeamID=0&VsConferenc'\
                'e=&VsDivision=&mode=Advanced&showDetails=0&showShots=1&sh'\
                'owZones=0'
        self.response = requests.get(self.url, headers=headers)
        self.json_data = self.response.json()

    def get_shot_data(self):
        """Returns pandas DataFrame of shot chart data for a certain player"""
        shot_data = self.json_data['resultSets'][0]['rowSet']
        data_headers = self.json_data['resultSets'][0]['headers']
        data_frame = pandas.DataFrame(data=shot_data, columns=data_headers)
        return data_frame

    def plot_data(self, x, y):
        seaborn.set_style("white")
        seaborn.set_color_codes()
        plt.figure(figsize=(12, 10))
        plt.scatter(x, y)
        plt.show()
