import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)

plt.plot(x, 1./np.exp(2*x[0]) - 1./np.exp(2*x) + np.log(x+1)/2.,
        lw=2, label='Excel')
plt.plot(x, np.exp(x)/2000., lw=2, label='Python')
plt.plot(x, np.log(x+1)/2. + np.exp(x)/2300., lw=2, label='This Tutorial')

plt.xlabel('Time Investment', fontsize=16)
plt.xticks( [] )

plt.ylabel('Productivity', fontsize=16)
plt.yticks( [] )

plt.legend(loc=2)
plt.show()