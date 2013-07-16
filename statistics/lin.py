import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps
# This seeds the random number generator so that it always returns the same
# numbers
np.random.seed(20)

x = np.linspace(0, 20, 6)

y_clean = 2.3*x + 1.2

y_noise = y_clean + 2.5*np.random.randn( x.shape[0] )

sps_fit = sps.linregress(x, y_noise)
sps_slope, sps_int, sps_r, sps_p, sps_stderr = sps_fit
#print sps_slope, sps_int, sps_r**2

sps_resid = y_noise - (sps_slope*x + sps_int)

np_fit = np.polyfit(x, y_noise, deg=1)
np_poly = np.poly1d( np_fit )
#print np_fit

poly_resid = y_noise - np_poly(x)

plt.figure()

plt.plot(x, y_clean, 'o', ms=10, label='Clean data')
plt.plot(x, y_noise, 'o', ms=10, label='Noisy data')

plt.plot(x, sps_slope*x + sps_int, 'r-', label='Scipy')
plt.plot(x, np_poly(x), 'k--', label='Numpy')

plt.title('Data and Fit Lines')
plt.legend(loc=2)

plt.figure()

plt.plot(x, sps_resid, 'ro-', ms=10, label='Scipy')
plt.plot(x, poly_resid, 'bo-', ms=10, label='Numpy')

plt.xlim(x[0]-2, x[-1]+2)
plt.title('Residuals')
plt.legend(loc=2)

plt.show()
