import utilities.data as data_utils
import utilities.config as config
from classes.Game import Game
import datetime
import pandas as pd
import os


def is_lock(game: Game, diff_threshold=5, pct_threshold=75, market="open"):

    if market == "open":
        if game.favorite_diff_open == "home":
            diff = game.home_diff_open
            pct = game.home_pct
        else:
            diff = game.away_diff_open
            pct = game.home_pct
    else:
        if game.favorite_diff_open == "home":
            diff = game.home_diff_close
            pct = game.home_pct
        else:
            diff = game.away_diff_close
            pct = game.home_pct

    return diff >= diff_threshold and pct >= pct_threshold

