import numpy as np
import matplotlib.pyplot as plt


def voltage_spectra(data, volt):

    """
    Given raw data from the Pico sampler and the
    voltage setting used for the collection, computes
    the voltage spectra including frequency values

    Parameters: data - array of Pico sampler data
                volt - (int) voltage range used in sampling in mV

    Returns: freqs - frequency array
             voltage - voltage spectrum
    """

    converted = data*volt/2**15
    voltage = np.fft.fft(converted)
    freqs = np.fft.fftfreq(len(converted))

    return freqs, voltage


def power_spectra(data, volt):

    """
    Calculates the power spectrum and frequency values
    given raw data from the Pico sampler.

    :param data: raw data from Pico sampler
    :param volt: (int) voltage range used in sampling in mV
    :return: freqs: frequency array associated with the power spectrum,
    power: array of power magnitude values for the spectra

    """

    freqs, voltage = voltage_spectra(data, volt)
    power = np.abs(voltage)**2

    return freqs, power


def plot_power(power, name):

    """
    Given the power magnitudes of a spectrum computed
    with np.fft.fft, produces the frequencies and shifts all values
    for proper plotting with negative frequencies to the left
    and positive to the right. Saves the figure with a the name
    given as argument append with "plot.pdf".

    :param power: (array) power magnitude values from np.fft.fft
    :param name: (str) name to give the spectrum
    """

    freqs = np.fft.fftfreq(len(power), 7/62.5)
    powershift = np.fft.fftshift(power)
    freqsshift = np.fft.fftshift(freqs)

    plt.plot(freqsshift, powershift)
    plt.title("Power Spectrum of " + name)
    plt.ylabel("Power")
    plt.xlabel("Frequency")
    plt.savefig(name + "plot.pdf")
    plt.show()


def gain(Tcal, scal, scold):
    
    """
    Calculates the gain value for intensity calibration 
    assuming the temperature of the sky is negligible compared
    to the temperature of the calibration source.

    :param Tcal: (int) temperature in Kelvin of the calibration
    source.
    :param scal: (array) power spectrum of the calibration source
    :param scold: (array) power spectrum of the cold sky
    :returns (float) calculated gain value of the system 
    """

    G = Tcal*np.sum(scold)/(np.sum(scal - scold))
    return G


def avg_spec(filepath):

    """
    Calculates the average power spectrum on the assumption
    that there are 10 datafiles (.npz) formatted with [A, A, A, ... 
    B, B, B] with A and B referring to the respective ports on the 
    Pico sampler. Assumes port A has imaginary values and port B 
    real values. File names must be the same name appended with 
    i an integer from 0 to 9. Data saved into the .npz file should
    have a key of 'data'. Saves the mean spectra as the filepath + 
    mean.npz.
    
    :param filepath: (str) filepath to the datafiles
    :return: (array) average spectrum power values, 
    frequencies not included.
    """

    imag = np.array([])
    real = np.array([])

    for i in range(10):
        npz = np.load(filepath + str(i) + '.npz')
        data = npz['data']
        data.shape = (2, -1)
        imag = np.append(imag, data[0])
        real = np.append(real, data[1])

    datac = 1j * imag * 0.025 / (2 ** 15) + (real * 0.025 / (2 ** 15))
    datac.shape = (-1, 16000)
    ft_data = np.fft.fft(datac, axis=1)
    meanspec = np.mean(np.abs(ft_data) ** 2, axis=0)

    np.savez(filepath + 'mean', data=meanspec)

    return meanspec


def mean_smoothing(freqs, data, groupsize):
    """
    This function splits the given data and frequencies into
    roughly equally sized bins according to groupsize, averages
    the values within the bins, and returns the averaged frequencies
    and data.

    :param freqs: (array) frequency values
    :param data: (array) amplitude values
    :param groupsize: (int) roughly how many datapoints in each
    bin
    :return: Mean smoothed data with corresponding frequencies
    """

    blocks = len(data)/groupsize

    data = np.array_split(data, blocks)
    meandata = [np.mean(i) for i in data]
    freqs = np.array_split(freqs, blocks)
    meanfreqs = [np.mean(i) for i in freqs]

    return meanfreqs, meandata
