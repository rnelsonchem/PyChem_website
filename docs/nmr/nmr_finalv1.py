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
plt.yticks([]) # Remove tick labels by setting to an empty list
plt.tick_params(top='off') # Remove top ticks
plt.xlim(8.9, 0.5)
plt.ylim(-1.0e6, 6e7)
plt.xlabel('ppm')

# Let's make an inset to this figure as well
# The list argument is location and size parameters for the inset
# See the axes documentation for the meaning of these values
plt.axes([0.2, 0.45, 0.4, 0.4])

# All the same as above
plt.plot(ppm, intensity, '-')
plt.xlim(8.9, 0.5)
plt.yticks([])
plt.tick_params(top='off')
plt.xlim(8.7, 6.6)
plt.ylim(-1.0e5, 0.5e7)

plt.show()

