import matplotlib.pyplot as plt


# mean_percentage: must be form 0 to 1; if value is 0, then nothing will be ha
def plot_history(dictionary, title="", x_axis_name="X", y_axis_name="Y"):
    for name, arr in dictionary.items():
        plt.plot(arr, label=name)

    # naming the x axis
    plt.xlabel(x_axis_name)
    # naming the y axis
    plt.ylabel(y_axis_name)
    # giving a title to my graph
    plt.title(title)

    # show a legend on the plot
    plt.legend(loc="lower left")

    # function to show the plot
    plt.show()
