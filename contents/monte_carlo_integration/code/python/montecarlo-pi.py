import numpy as np


def in_circle(x_pos, y_pos):
    r = 1
    return x_pos ** 2 + y_pos ** 2 < r ** 2


def monte_carlo(n):
    pi_count = 0
    for i in range(n):
        point_x = np.random.rand()
        point_y = np.random.rand()

        if in_circle(point_x, point_y):
            pi_count = pi_count + 1
    pi_estimate = 4 * pi_count / n
    pi_error = 100 * abs(pi_estimate - np.pi) / np.pi
    print("The pi estimate is:", pi_estimate)
    print("Percent error is:", pi_error, "%")


monte_carlo(10000000)
