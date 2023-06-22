import numpy as np
import matplotlib.pyplot as plt

def plot_sin_curve(accuracy):
    degrees = np.arange(0, 360, accuracy)
    radians = np.radians(degrees)
    sine_values = np.sin(radians)
    plt.plot(degrees, sine_values)
    plt.xlabel('Grad')
    plt.ylabel('Sinus')
    plt.show()

accuracy = float(input("Bitte gib die Genauigkeit in Grad an: "))
plot_sin_curve(accuracy)