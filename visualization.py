import logging
import matplotlib.pyplot as plt
from matplotlib import style
import pandas

logger = logging.getLogger("HAUSARBEIT")


class Visualization:
    def __init__(self, dataframe, dataframe_name):
        self.dataframe = dataframe
        self.name = dataframe_name

    def create_plot_from_dataframe(self):
        df = self.dataframe
        style.use("ggplot")

        # resize graph
        plt.figure(figsize=(15, 8))
        # plot all the lines from
        for y_index in df:
            if y_index != "x":
                plt.plot(df.x, df[y_index], label=y_index)

        plt.legend(loc=(1.01, 0.0))
        plt.grid(True, color="k")
        plt.title(df.name)
        plt.ylabel("y-axis")
        plt.xlabel("x-axis")
        logger.info("Show plot: " + self.name)
        plt.show()
