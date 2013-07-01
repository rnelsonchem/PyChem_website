import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps

x = np.linspace(0, 20, 6)

y_clean = 2.3*x + 1.2

y_noise = y_clean + 2.5*np.random.randn( x.shape[0] )

sps_fit = sps.linregress(x, y_noise)
sps_slope, sps_int, sps_r, sps_p, sps_stderr = sps_fit
#print sps_slope, sps_int, sps_r**2

np_fit = np.polyfit(x, y_noise, deg=1)
np_poly = np.poly1d( np_fit )
#print np_fit

plt.plot(x, y_clean, 'o', ms=10, label='Clean data')
plt.plot(x, y_noise, 'o', ms=10, label='Noisy data')

plt.plot(x, sps_slope*x + sps_int, 'r-', label='Scipy')
plt.plot(x, np_poly(x), 'k--', label='Numpy')

plt.legend(loc=2)
plt.show()
