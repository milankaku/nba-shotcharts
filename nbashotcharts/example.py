import api


def main():
    shot_data = api.ShotData()
    shot_chart = shot_data.get_shot_data()
    shot_data.plot_data(shot_chart.LOC_X, shot_chart.LOC_Y)

if __name__ == "__main__":
    main()
