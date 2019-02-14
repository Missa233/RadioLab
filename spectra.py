import numpy as np
import matplotlib as plt

def voltage_spectra(data, volt):
    converted = data*volt/2**15
    voltage = np.fft.fft(converted)
    freqs = np.fft.fftfreq(len(converted))

    return freqs, voltage


def power_spectra(data, volt):
    freqs, voltage = voltage_spectra(data, volt)
    power = np.abs(voltage)**2

    return freqs, power


def plot_power(data, volt, name):
    freqs, power = power_spectra(data, volt)
    powershift = np.fft.fftshift(power)
    freqsshift = np.fft.fftshift(freqs)

    plt.plot(freqsshift, powershift)
    plt.title("Power Spectrum of " + name)
    plt.ylabel("Power")
    plt.xlabel("Frequency")
    plt.show()