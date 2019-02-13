import ugradio
import numpy as np
import matplotlib.pyplot as plt


def collect1st(volt_range):
    """volt_range: str """
    first_data = ugradio.pico.capture_data(volt_range, divisor=10, dual_mode=True)
    np.savetxt('firsthorn', first_data)

    plt.histogram(first_data)
    plt.savefig('firsthist.pdf')

    return np.loadtxt("firsthorn")

def insert_upper(volt_range):
    data = ugradio.pico.capture_data(volt_range, divisor=10, dual_mode=True)
    np.savetxt('uppertestsig', data)

    return np.loadtxt('uppertestsig')


def insert_lower(volt_range):
    data = ugradio.pico.capture_data(volt_range, divisor=10, dual_mode=True)
    np.savetxt('lowertestsig', data)

    return np.loadtxt('lowertestsig')



