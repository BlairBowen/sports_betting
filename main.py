from src.find_locks import find_locks
import utilities.data as data_utils
import utilities.config as config
import os
import pandas as pd

def main() -> None:
    locks = find_locks(sport="nba", diff_threshold=10, pct_threshold=0)
    print(locks)
    locks.to_csv("data/locks.csv")
    pass


if __name__ == "__main__":
    main()
