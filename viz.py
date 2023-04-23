from matplotlib import pyplot as plt

labels = {"LABEL_0": "sad",
          "LABEL_1": "good-vibes",
          "LABEL_2": "aggressive"
          }


def plot_song_themes(df):
    df["label"] = df["label"].replace(labels)
    fig, ax = plt.subplots()
    ax.bar(df["label"], df["score"])
    ax.set_title("Label Scores")
    ax.set_xlabel("Label")
    ax.set_ylabel("Score")

    return plt.gcf()
