import numpy as np
import matplotlib.pyplot as plt

def plot_chart():
    # Данные для графика
    fig, ax = plt.subplots()

    L = 6
    x = np.linspace(0, L)
    ncolors = len(plt.rcParams['axes.prop_cycle'])
    shift = np.linspace(0, L, ncolors, endpoint=False)
    for s in shift:
        ax.plot(x, np.sin(x + s), 'o-')
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    ax.set_title('График darkplotlib')

    fig.savefig("dark_test.png")
    plt.show()
