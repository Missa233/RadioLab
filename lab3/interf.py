import numpy as np
import ugradio as ug
import scipy.consts as consts


def find_fringe(utime, ra, dec, Bew, Bns):

    """
    Calculates the min and max expected fringe frequencies
    :param utime: (array) observation times in Unix time
    :param ra: (float) RA of observed object (degrees)
    :param dec: (float) DEC of observed object (degrees)
    :param Bew: (float) East-West component of interferometer
    baseline in meters
    :param Bns: (float) North-South component of interferometer
    baseline in meters
    :return: minimum fringe frequency, maximum fringe frequency
    """

    JDtime = ug.timing.julian_date(utime)
    LSTtime = ug.timing.lst(jd=JDtime)
    h = LSTtime - ra
    l = consts.c/10.7e9
    L = ug.coord.nch.lat
    Qew = Bew*np.cos(d)/l
    Qns = Bns*np.sin(L)*np.cos(d)/l

    ff = Qew*np.cos(h) - Qns*np.sin(h)

    return min(ff), max(ff)