from matplotlib import pyplot as plt

labels = ["sad", "good-vibes", "aggressive"]


def plot_song_themes(df):
    plt.bar(labels, 100 * df["score"], color='C0')
    plt.title("New Song Classification")
    plt.ylabel("Class probability (%)")

    return plt.gcf()
