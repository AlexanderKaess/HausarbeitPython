import logging
import matplotlib.pyplot as plt
from matplotlib import style

logger = logging.getLogger("HAUSARBEIT")


class Visualization:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def create_plot_from_dataframe(self):
        df = self.dataframe
        style.use("ggplot")

        fig, ax = plt.subplots(figsize=(8,8))
        ax.plot(df)

        ax.legend(df)
        ax.grid(True, color="k")
        plt.title(df.name)
        plt.ylabel("y-axis")
        plt.xlabel("x-axis")
        logger.info("Show plot")
        plt.show()
