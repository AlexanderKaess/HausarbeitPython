import logging
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
import pandas

logger = logging.getLogger("HAUSARBEIT")


class Visualization:
    def __init__(self, *args):
        if isinstance(args[0], pd.DataFrame):
            self.source_dataframe = args[0]
            logger.info("source-dataframe: " + self.source_dataframe.name)

        if len(args) > 1:
            if isinstance(args[1], pd.DataFrame):
                self.selector_dataframe = args[1]
                logger.info("selector-dataframe: " + self.selector_dataframe.name)
            else:
                logger.info("args are no valid dataframe object[1]")
                self.selector_dataframe = pd.DataFrame(args[1])

    def create_plot_from_dataframe(self):
        try:
            df = self.source_dataframe
            style.use("ggplot")

            # resize graph
            plt.figure(figsize=(15, 8))
            # plot all the lines from source_dataframe
            for y_index in df:
                if y_index != "x":
                    plt.plot(df.x, df[y_index], label=y_index)

            plt.legend(loc=(1.01, 0.0))
            plt.grid(True, color="k")
            plt.title(df.name)
            plt.ylabel("y-axis")
            plt.xlabel("x-axis")
            logger.info("Show plot: " + df.name)
            plt.show()
        except:
            logger.info("get an exception at methode create_plot_from_dataframe")

    def create_plot_from_selection(self):
        df_source = self.source_dataframe
        df_selector = self.selector_dataframe
        style.use("ggplot")

        # resize graph
        plt.figure(figsize=(15, 8))
        # plot all the line from dataframes
        for y_index in df_source:
            print(y_index)
            if y_index != "x":
                plt.plot(df_source.x, df_source[y_index], label=y_index)
                #plt.plot(df_selector.index[0], df_selector[y_index], label=y_index, linestyle="dashed")

        plt.legend(loc=(1.01, 0.0))
        plt.grid(True, color="k")
        plt.title("best-fits")
        plt.ylabel("y-axis")
        plt.xlabel("x-axis")
        logger.info("Show plot: best-fits")
        plt.show()
