import numpy as np 
import matplotlib.pyplot as plt

wn, ab = np.loadtxt('ftir_data.txt', unpack=True)

plt.plot(wn, ab)

plt.xlim(4000, 1500)
plt.xlabel('Wavenumbers ($\mathrm{cm^{-1}}$)')
plt.ylim(0.25, 1.7)
plt.ylabel('Absorbance (a.u.)')

plt.title('My First IR data Set')

plt.grid()

plt.show()
