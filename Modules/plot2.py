import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x_sikap_biasa = np.arange(1, 15, 1)
x_c = np.arange(1,15,1)
x_m = np.arange(7,15,1)

biasa = fuzz.trapmf(x_sikap_biasa, [1, 1, 5, 7])
cukup = fuzz.trimf(x_c, [5, 7, 10])
mantap = fuzz.trimf(x_m, [7,10,1000])
plt.plot(x_sikap_biasa, biasa, 'b', linewidth=1.5, label='Buruk')
plt.plot(x_c, cukup, 'r', linewidth=1.5, label='Cukup')
plt.plot(x_m, mantap, 'g', linewidth=1.5, label='Sangat ramah')
plt.legend()
plt.show()