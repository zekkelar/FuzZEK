import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x_sikap_biasa = np.arange(0, 15, 1)
x_c = np.arange(1,15,1)

biasa = fuzz.trapmf(x_sikap_biasa, [0, 0, 5, 7])

cukup = fuzz.trimf(x_c, [5, 7, 10])

plt.plot(x_sikap_biasa, biasa, 'b', linewidth=1.5, label='Sangat Pendek')
plt.plot(x_c, cukup, 'b', linewidth=1.5, label='Sangat Pendek')

plt.show()