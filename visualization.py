import logging
import matplotlib.pyplot as plt
from matplotlib import style

logger = logging.getLogger("HAUSARBEIT")


class Visualization:
    def create_plot_from_dataframe(self, dataframe):
        style.use("ggplot")
        df = dataframe
        ax = plt.gca()

        df.plot(kind="line", x="x", y="y1", ax=ax, color="red")
        df.plot(kind="line", x="x", y="y2", ax=ax, color="blue")
        df.plot(kind="line", x="x", y="y3", ax=ax, color="green")
        df.plot(kind="line", x="x", y="y4", ax=ax, color="black")

        ax.grid(True, color="k")
        plt.title("Train data")
        plt.ylabel("y-axis")
        plt.xlabel("x-axis")
        logger.info("Show plot")
        plt.show()

    def create_alotplot_from_dataframe(self, dataframe):
        style.use("ggplot")
        df = dataframe
        ax = plt.gca()

        df.plot(kind="line", x="x", y="y1", ax=ax, color="red")
        df.plot(kind="line", x="x", y="y2", ax=ax, color="blue")
        df.plot(kind="line", x="x", y="y3", ax=ax, color="green")
        df.plot(kind="line", x="x", y="y4", ax=ax, color="black")

        ax.grid(True, color="k")
        plt.title("Ideal data")
        plt.ylabel("y-axis")
        plt.xlabel("x-axis")
        logger.info("Show plot")
        plt.show()
