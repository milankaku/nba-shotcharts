import requests
import pandas
import matplotlib.pyplot as plt
import seaborn

headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}


class ShotChart(object):

    def __init__(self, player_id, season='2016-17'):
        self.url = 'http://stats.nba.com/stats/shotchartdetail?CFID=33&CFPAR'\
                'AMS=' + str(season) + '&ContextFilter=&ContextMeasure=FGA&DateFrom=&D'\
                'ateTo=&GameID=&GameSegment=&LastNGames=0&LeagueID=00&Loca'\
                'tion=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&'\
                'PaceAdjust=N&PerMode=PerGame&Period=0&PlayerID=' + str(player_id) + '&Plu'\
                'sMinus=N&PlayerPosition=&Rank=N&RookieYear=&Season=' + str(season) + '&Seas'\
                'onSegment=&SeasonType=Regular+Season&TeamID=0&VsConferenc'\
                'e=&VsDivision=&mode=Advanced&showDetails=0&showShots=1&sh'\
                'owZones=0'

        self.response = requests.get(self.url, headers=headers)
        self.json_data = self.response.json()

    def plot_shots(self):
        data_frame = self.get_shot_data()
        seaborn.set_style("white")
        seaborn.set_color_codes()
        plt.figure(figsize=(12, 10))
        plt.scatter(data_frame.LOC_X, data_frame.LOC_Y)
        plt.show()

    def get_shot_data(self):
        """Returns pandas DataFrame of shot chart data for a certain player"""
        shot_data = self.json_data['resultSets'][0]['rowSet']
        data_headers = self.json_data['resultSets'][0]['headers']
        data_frame = pandas.DataFrame(data=shot_data, columns=data_headers)
        return data_frame
