import numpy as np
import matplotlib.pyplot as plt
vals = np.loadtxt('MnO.csv', delimiter=',', skiprows=1, usecols=(2,))
plt.hist(vals, bins=100)
plt.show()
