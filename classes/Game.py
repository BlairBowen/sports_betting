import utilities.config as config
import utilities.data as data_utils
import utilities.math as sbm


class Game:

    def __init__(
        self, game_id, home_ml_open, away_ml_open, home_ml_close, away_ml_close, sport
    ) -> None:
        # try:
        json_response = data_utils.fetch_data(
            config.sports[sport]["event"].replace("*", game_id),
            f"event_{sport}_{game_id}.json",
        )
        self.game_id = game_id
        self.home_team = json_response["boxscore"]["teams"][1]["team"]["displayName"]
        self.away_team = json_response["boxscore"]["teams"][0]["team"]["displayName"]
        self.home_ml_open = home_ml_open
        self.away_ml_open = away_ml_open
        self.home_ml_close = home_ml_close
        self.away_ml_close = away_ml_close
        self.home_pct = float(json_response["predictor"]["awayTeam"]["teamChanceLoss"])
        self.away_pct = float(json_response["predictor"]["awayTeam"]["gameProjection"])
        self.home_diff_open = self.home_pct - sbm.convert_ml_to_prob(self.home_ml_open)
        self.away_diff_open = self.away_pct - sbm.convert_ml_to_prob(self.away_ml_open)
        self.home_diff_close = self.home_pct - sbm.convert_ml_to_prob(
            self.home_ml_close
        )
        self.away_diff_close = self.away_pct - sbm.convert_ml_to_prob(
            self.away_ml_close
        )
        self.favorite_ml_open = (
            "home" if self.home_ml_open > self.away_ml_open else "away"
        )
        self.favorite_ml_close = (
            "home" if self.home_ml_close > self.away_ml_close else "away"
        )
        self.favorite_pct = "home" if self.home_pct > self.away_pct else "away"
        self.favorite_diff_open = (
            "home" if self.home_diff_open > self.away_diff_open else "away"
        )
        self.favorite_diff_close = (
            "home" if self.home_diff_close > self.away_diff_close else "away"
        )
        # self.play = (
        #     (self.home_team, self.home_diff, self.home_pct)
        #     if self.home_diff > self.away_diff
        #     else (self.away_team, self.away_diff, self.away_pct)
        # )
        # # self.lock = True if self.play[1] >= diff_threshold and self.play[2] >= pct_threshold else False
        # self.lock = True if self.play[1] >= diff_threshold and self.play[2] >= pct_threshold else False
        # except Exception as e:
        #     print(f"failed to init Game for {self.away_team} v. {self.away_team}: {e}")
