import numpy as np
import matplotlib.pyplot as plt

# Read the values from the data file
vals = np.loadtxt('MO.csv', delimiter=',', skiprows=1, usecols=(2,))

# Set some default parameters
plt.rc('font', size=16)
# Change tick sizes
plt.rc('xtick.major', size=6, width=1.5)
plt.rc('ytick.major', size=6, width=1.5)
plt.rc('xtick.minor', size=3, width=1.)
plt.rc('ytick.minor', size=3, width=1.)
plt.rc('axes', linewidth=1.5)

# Create the initial histogram
plt.hist(vals, bins=100)

# x axis info
# This gets rid of the first and last tick label from default
plt.xlim(1.21, 2.59) 
# See here for Angstrom unicode
# http://matplotlib.1069221.n5.nabble.com/Fwd-Issues-with-TeX-symbols-and-font-changes-td14427.html
plt.xlabel(u'Distance (\u00c5)')

# y axis info
plt.ylim(-40, 1820)
plt.ylabel('Frequency')

plt.title('Manganese Oxygen Distances')

# Add minor ticks
plt.minorticks_on()
# Put the dotted line grid on the major axes
plt.grid()
# Resize everything for a tight fit in the figure window
plt.tight_layout()

plt.show()
