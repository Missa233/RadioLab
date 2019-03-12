import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt


def find_lambda(data):

    """
    This function takes in an array of arrays where each
    sub-array contains the measured null values in the waveguide
    for a given frequency and shorted combination. (i.e. 7GHz data
    with the waveguide shorted vs. 7GHz with waveguide open.) The
    function returns the best fit wavelength values based on the lab
    handout equation 5.

    :param data: (array) Array of arrays containing null position values
    :return : (list) best-fit wavelength values
    """

    def xm(m, A, l):
        return A + m * l / 2

    params = []
    lambdas = []
    for array in data:
        x = np.arange(1, len(array) + 1)
        y = array
        param = opt.curve_fit(xm, x, y)[0]
        params.append(param)
        lambdas.append(param[1])

    for i in range(len(data)):
        y = data[i]
        x = np.arange(1, len(y) + 1)
        paramsarr = params[i]
        print(paramsarr)
        plt.plot(x, y, 'ro')
        plt.plot(x, xm(x, paramsarr[0], paramsarr[1]))
        plt.show()

    return lambdas
