import utilities.api as api
import utilities.data as data_utils
import utilities.config as config
import utilities.math as sbm
import os
import pandas as pd
import datetime

picks = [250, -110, -320]


def main() -> None:
    print(api.get_todays_game(sport="ncaam"))
    pass


if __name__ == "__main__":
    main()
