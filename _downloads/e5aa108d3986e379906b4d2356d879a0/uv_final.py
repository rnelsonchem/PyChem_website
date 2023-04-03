import numpy as np
import matplotlib.pyplot as plt

# This function allows you to customize certain behavior of Matplotlib plots
# See: http://matplotlib.org/users/customizing.html
plt.rc('font', size=16)
plt.rc('axes', linewidth=1.5)
plt.rc('xtick.major', size=8, width=1.5)
plt.rc('ytick.major', size=8, width=1.5)

wn, ab = [], []

data_file = open('uv_data.txt')

for line in data_file:
    sp = line.split(',')
    wn.append( sp[0] )
    ab.append( sp[1] )

data_file.close()

wn = np.array(wn, dtype=float)
ab = np.array(ab, dtype=float)

plt.plot(wn, ab, 'g', lw=2)
plt.xlim(500,750)
plt.ylim(-0.005, 0.05)

plt.title('UV/Vis Spectrum of Compound 1')
plt.xlabel('Wavenumbers ($\mathrm{cm^{-1}}$)')
plt.ylabel('Absorbance (a.u.)')

plt.show()

