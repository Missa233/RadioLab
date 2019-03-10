import ugradio
import numpy as np


def collect(volt_range, blocks, name, numrepeat=1):

    """Uses ugradio.pico.capture_data to collect data
    with a sampling rate of 8.93 MHz with dual_mode = True.
    Can be used to make multiple calls to capture_data when
    more data than the maximum nblocks value capture_data
    will allow is needed. Saves a total of numrepeat .npz
    files with data indexed with the key 'data'.

    :param volt_range: (str) voltage range to capture data at
    :param blocks: (int) number of 16,000 complex sampled sets
    to collect in one call to capture_data
    :param numrepeat: (int) number of times to repeat the call
    to capture_data
    :param name: (str) name to save the data file with, appended
    with i in range(0, numrepeat) for each datafile.
    """

    for i in range(0, numrepeat):
        data = ugradio.pico.capture_data(volt_range, divisor=7, dual_mode=True, nblocks=blocks)
        np.savez(name + str(i), data=data)
