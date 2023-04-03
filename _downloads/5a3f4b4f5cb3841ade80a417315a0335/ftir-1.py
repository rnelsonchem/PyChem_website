import numpy as np
import matplotlib.pyplot as plt

wn, ab = np.loadtxt('ftir_data.txt', unpack=True)

plt.plot(wn, ab)
plt.xlim(4000, 1400)
plt.ylim(0.2, 1.6)

plt.show()