import numpy as np
import matplotlib.pylab as plt

data_file = open('nmr_data.txt')

intensity = []

for line in data_file:
    if 'LEFT' in line:
        sp = line.split()
        left = float(sp[3])
        right = float(sp[-2])

    elif 'SIZE' in line:
        sp = line.split()
        size = int(sp[3])

    elif line[0] == '#':
        continue

    else:
        intensity.append( line )

ppm = np.linspace(left, right, size)
intensity = np.array(intensity, dtype=float)

plt.plot(ppm, intensity, '-')
plt.xlim(8.9, 0.5)
plt.yticks([])
plt.tick_params(top='off')

plt.show()