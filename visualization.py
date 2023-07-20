import logging
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style

logger = logging.getLogger("HAUSARBEIT")


class Visualization:
    """
    A class to represent a visualization.

    Methods
    -------
    create_plot_from_dataframe:
        Create a plot from a dataframe
    create_plot_from_selection:
        Create a plot from a dataframe with a selection from another dataframe
    """

    def __init__(self, *args):
        """
        Constructs all the necessary attributes for the visualization object.
                Parameters:
                    source_dataframe (dataframe): source of data to plot
                    selector_dataframe (dataframe): selection for witch the data is visualized
        """
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
        """
        Create a plot from a dataframe
        """
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
        """
        Create a plot from a dataframe with a selection from another dataframe
        """
        logger.info("Create plot from selection")
        df_source = self.source_dataframe
        df_selector = self.selector_dataframe
        style.use("ggplot")

        # resize graph
        plt.figure(figsize=(15, 8))
        # plot all the line from dataframes
        logger.info("Create plot source dataframe")
        for columns_source in df_source:
            if columns_source != "x":
                plt.plot(df_source.x, df_source[columns_source], label=columns_source)

        logger.info("Create plot selector dataframe")
        for columns_selector in df_selector:
            if columns_selector != "x":
                plt.plot(df_selector.x, df_selector[columns_selector], label=columns_selector, linestyle="dashed")

        plt.legend(loc=(1.01, 0.0))
        plt.grid(True, color="k")
        plt.title("best-fits")
        plt.ylabel("y-axis")
        plt.xlabel("x-axis")
        logger.info("Show plot: best-fits")
        plt.show()
