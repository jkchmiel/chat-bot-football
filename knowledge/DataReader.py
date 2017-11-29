import pandas as pd
import os

SOURCE_DATA = os.path.join(os.path.dirname(__file__), "data/football_stats.csv")


def read_data():
    return pd.read_csv(SOURCE_DATA)


