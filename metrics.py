import numpy as np

def add_metrics(df):
    df["goals90"] = df["goals"] / df["min"] * 90
    df["assists90"] = df["assists"] / df["min"] * 90

    df["finishing_efficiency"] = np.where(df["xG"] > 0, df["goals"] / df["xG"], 0)
    df["creativity_efficiency"] = np.where(df["xA"] > 0, df["assists"] / df["xA"], 0)

    df["threat_score"] = df["xG90"] + df["xA90"]

    return df
