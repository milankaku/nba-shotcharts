import api


def main():
    shot_data = api.ShotData()
    shot_chart = shot_data.get_shot_data()
    print(shot_chart.head())

if __name__ == "__main__":
    main()
