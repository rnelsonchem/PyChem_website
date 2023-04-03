import numpy as np 
import matplotlib.pyplot as plt

wn, ab = np.loadtxt('ftir_data.txt', unpack=True)

plt.plot(wn, ab)

plt.xlim(4000, 1500)
# This label uses a special formatting called 'MathText', which is a subset of
# TeX that is built into Matplotlib. This automatically italicises things,
# which is reset by the mathrm command. See:
# http://matplotlib.org/users/mathtext.html
plt.xlabel('Wavenumbers ($\mathrm{cm^{-1}}$)')
plt.ylim(0.25, 1.7)
plt.ylabel('Absorbance (a.u.)')

plt.title('My First IR Data Set')

plt.grid()

plt.show()
