import pandas as pd
from src.constants import columns

def load_data(path):
    df = pd.read_csv(path, header=None, sep=",")
    df.columns = columns
    return df

def preprocess_data(df):
    # drop unused column
    df = df.drop("difficulty_level", axis=1)

    # convert label
    df["label"] = df["label"].astype(str)
    df["label"] = df["label"].apply(lambda x: 0 if x == "normal" else 1)

    return df