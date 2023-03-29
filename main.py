"""

Description: Python script for stats learning purposes.

"""
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
from matplotlib import pyplot as plt
import random
import brownian


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def plot_stock_price(mu, sigma):
    """
    Plots stock price for multiple scenarios
    """
    plt.figure(figsize=(9, 4))
    for i in range(5):
        plt.plot(b.stock_price(mu=mu,
                               sigma=sigma,
                               dt=0.1))
    plt.legend(['Scenario-' + str(i) for i in range(1, 6)],
               loc='upper left')
    plt.hlines(y=100, xmin=0, xmax=520,
               linestyle='--', color='k')
    plt.show()


def random_walk_2d(n):
    # creating two array for containing x and y coordinate
    # of size equals to the number of size and filled up with 0's
    x = np.zeros(n)
    y = np.zeros(n)

    # filling the coordinates with random variables
    for i in range(1, n):
        val = random.randint(1, 4)
        if val == 1:
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1]
        elif val == 2:
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1]
        elif val == 3:
            x[i] = x[i - 1]
            y[i] = y[i - 1] + 1
        else:
            x[i] = x[i - 1]
            y[i] = y[i - 1] - 1

    plt.title("Random Walk ($n = " + str(n) + "$ steps)")
    plt.plot(x, y)
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # defining the number of steps
    n_steps = 100000

    b = brownian.Brownian(0)
    w = b.gen_random_walk(n_steps)

    # plt.title("Random Walk ($n = " + str(n_steps) + "$ steps)")
    # plt.plot(range(n_steps), w)
    # plt.show()

    plot_stock_price(0.2, 0.65)

    # random_walk_2d(n_steps)
