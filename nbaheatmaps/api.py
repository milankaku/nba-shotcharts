import requests
import pandas
import matplotlib.pyplot as plt
import seaborn
import urllib.request
from matplotlib.patches import Arc, Rectangle, Circle

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
        self.player_id = player_id
        self.response = requests.get(self.url, headers=headers)
        self.json_data = self.response.json()
        seaborn.set_style("white")
        seaborn.set_color_codes()

    def plot_shots(self):
        data_frame = self.get_shot_data()
        plt.figure(figsize=(12, 11))
        plt.scatter(data_frame.LOC_X, data_frame.LOC_Y)
        self.draw_court()
        self.get_image(self.player_id)
        plt.xlim(-300, 300)
        plt.show()

    def get_shot_data(self):
        """Returns pandas DataFrame of shot chart data for a certain player"""
        shot_data = self.json_data['resultSets'][0]['rowSet']
        data_headers = self.json_data['resultSets'][0]['headers']
        data_frame = pandas.DataFrame(data=shot_data, columns=data_headers)
        return data_frame

    def draw_court(self, ax=None):
        if ax is None:
            ax = plt.gca()

        # Create the basketball court
        basketball_hoop = Circle((0,0), radius=9, color='black', linewidth=2, fill=False)
        paint_outer = Rectangle((-80, -47.5), 160, 190, linewidth=2, color='black', fill=False)
        paint_inner = Rectangle((-60, -47.5), 120, 190, linewidth=2, color='black', fill=False)
        freethrow_arc =  Arc((0, 142.5), 120, 120, theta1=0, theta2=180,
                             linewidth=2, color='black', fill=False)
        bottom_freethrowarc = Arc((0, 142.5), 120, 120, theta1=180, theta2=0,
                                linewidth=2, color='black', linestyle='dashed')

        restricted_zone = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=2,
                         color='black')
        center_court_outer = Arc((0, 422.5), 120, 120,theta1=180, theta2=0, linewidth=2, color='black')
        center_court_inner = Arc((0, 422.5), 40, 40, theta1=180, theta2=0, linewidth=2, color='black')
        out_lines = Rectangle((-250, -47.5), 510, 470, linewidth=2, color='black', fill=False)


        backboard = Rectangle((-27, -7.5), 60, 1, linewidth=2, color='black')

        threepoint_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=2, color='black')
        right_corner = Rectangle((-220, -47,5), 0, 140, linewidth=2, color='black')
        left_corner = Rectangle((220, -47,5), 0, 140, linewidth=2, color='black')

        full_court = [freethrow_arc, restricted_zone, bottom_freethrowarc,  basketball_hoop,
                      paint_inner, paint_outer, backboard, center_court_inner, right_corner, left_corner, out_lines, center_court_outer, threepoint_arc]

        for element in full_court:
            ax.add_patch(element)

        return ax

    def get_image(self, player_id):
        image = urllib.request.urlretrieve("http://stats.nba.com/media/players/230x185/" + str(player_id) + ".png",
                                 str(player_id) + ".png")
        player_image = plt.imread(image[0])
        plt.imshow(player_image)