import api


def main():
    # Example player_ids = [Jimmy Butler: 202710, JJ Redick: 203584]
    shots = api.ShotChart(player_id=203584)
    shots.plot_shots()

if __name__ == "__main__":
    main()
