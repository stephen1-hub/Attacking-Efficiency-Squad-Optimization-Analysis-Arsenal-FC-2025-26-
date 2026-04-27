import matplotlib.pyplot as plt

def plot_finishing(df):
    plt.figure(figsize=(8,6))
    plt.scatter(df["xG"], df["goals"])

    for i in range(len(df)):
        plt.text(df["xG"][i], df["goals"][i], df["player"][i], fontsize=8)

    plt.plot([0, df["xG"].max()], [0, df["xG"].max()])
    plt.xlabel("Expected Goals (xG)")
    plt.ylabel("Actual Goals")
    plt.title("Finishing Efficiency")

    plt.savefig("outputs/finishing_plot.png")
    plt.show()
