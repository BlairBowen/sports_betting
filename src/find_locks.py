import utilities.data as data_utils
import utilities.config as config
from classes.Game import Game
import datetime
import pandas as pd


def find_locks(sport, diff_threshold = 5, pct_threshold = 75):
    todays_date = datetime.date.today().strftime("%Y%m%d")
    json_response = data_utils.fetch_data(
        config.sports[sport]["scoreboard"].replace("*", todays_date),
        f"scoreboard_{sport}_{todays_date}.json"
    )

    game_list = list()

    game_df = pd.DataFrame(columns = [
        "id",
        "home_team",
        "away_team",
        "home_ml_open",
        "away_ml_open",
        "home_ml_close",
        "away_ml_close",
        "home_pct",
        "away_pct",
        "home_diff_open",
        "away_diff_open",
        "home_diff_close",
        "away_diff_close",
        "favorite_ml_open",
        "favorite_ml_close",
        "favorite_pct",
        "favorite_diff_open",
        "favorite_diff_close",
    ])

    for game in json_response["events"]:
        try:
            home_ml_open = game["competitions"][0]["odds"][0]["moneyline"]["home"]["open"]["odds"]
            away_ml_open = game["competitions"][0]["odds"][0]["moneyline"]["away"]["open"]["odds"]
            home_ml_close = game["competitions"][0]["odds"][0]["moneyline"]["home"]["close"]["odds"]
            away_ml_close = game["competitions"][0]["odds"][0]["moneyline"]["away"]["close"]["odds"]
            game_play = Game(game["id"], home_ml_open, away_ml_open, home_ml_close, away_ml_close, sport)
            game_list.append(game_play)
        except Exception as e:
            game_name = game["shortName"]
            print(f"failed to init {game_name}: {e}")

    for play in game_list:
        new_row = {
            "id": play.game_id,
            "home_team": play.home_team,
            "away_team": play.away_team,
            "home_ml_open": play.home_ml_open,
            "away_ml_open": play.away_ml_open,
            "home_ml_close": play.home_ml_close,
            "away_ml_close": play.away_ml_close,
            "home_pct": play.home_pct,
            "away_pct": play.away_pct,
            "home_diff_open": play.home_diff_open,
            "away_diff_open": play.away_diff_open,
            "home_diff_close": play.home_diff_close,
            "away_diff_close": play.away_diff_close,
            "favorite_ml_open": play.favorite_ml_open,
            "favorite_ml_close": play.favorite_ml_close,
            "favorite_pct": play.favorite_pct,
            "favorite_diff_open": play.favorite_diff_open,
            "favorite_diff_close": play.favorite_diff_close,
        }
        game_df.loc[len(game_df)] = new_row

    return game_df
    # return game_df.loc[(game_df["home_diff_open"] >= diff_threshold) | (game_df["away_diff_open"] >= diff_threshold)][["id", "home_team", "away_team", "home_diff_open", "away_diff_open"]]

